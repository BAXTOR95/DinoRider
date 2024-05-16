import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from dino_game.config import GAME_URL


class DinoGame:
    """
    A class to represent the Chrome Dino game and control its actions using Selenium.

    Attributes:
    -----------
    chrome_options : webdriver.ChromeOptions
        The options for the Chrome WebDriver.
    driver : webdriver.Chrome
        The Chrome WebDriver instance.
    """

    def __init__(self):
        """Initialize the DinoGame with Chrome WebDriver and game settings."""
        self.chrome_options = self._get_chrome_options()
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self._load_game()

    def _get_chrome_options(self):
        """
        Configure Chrome options for the WebDriver.

        Returns:
        --------
        webdriver.ChromeOptions
            The configured Chrome options.
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--window-size=800,600")  # Set a fixed window size
        return chrome_options

    def _load_game(self):
        """Load the Chrome Dino game in the WebDriver."""
        try:
            self.driver.get(GAME_URL)
            # Wait for the game to load completely
            time.sleep(3)
        except WebDriverException as e:
            pass

    def start_game(self):
        """Start the Chrome Dino game by sending a space key press."""
        self._send_key(Keys.SPACE)

    def jump(self):
        """Make the Dino jump by sending an up arrow key press."""
        self._send_key(Keys.ARROW_UP)

    def duck(self, duration=0.5):
        """
        Make the Dino duck by sending a down arrow key press.

        Parameters:
        -----------
        duration : float, optional
            The duration to hold the duck position in seconds (default is 0.5).
        """
        self._send_key_event(40, 'keydown')  # Send down arrow key press
        time.sleep(duration)
        self._send_key_event(40, 'keyup')  # Release down arrow key press

    def _send_key(self, key):
        """
        Send a key press to the game.

        Parameters:
        -----------
        key : selenium.webdriver.common.keys.Keys
            The key to send.
        """
        self.driver.find_element(By.TAG_NAME, "body").send_keys(key)

    def _send_key_event(self, key_code, event_type):
        """
        Send a specific key event to the game using JavaScript.

        Parameters:
        -----------
        key_code : int
            The key code of the key event.
        event_type : str
            The type of key event ('keydown' or 'keyup').
        """
        script = f"""
        var e = new KeyboardEvent('{event_type}', {{'keyCode': {key_code}, 'which': {key_code}}});
        document.dispatchEvent(e);
        """
        self.driver.execute_script(script)

    def close(self):
        """Close the WebDriver and end the game session."""
        self.driver.quit()
