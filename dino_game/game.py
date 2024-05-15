import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from dino_game.config import GAME_URL


class DinoGame:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-popup-blocking")
        self.chrome_options.add_argument("--profile-directory=Default")
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.chrome_options.add_argument("--disable-plugins-discovery")
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_argument("disable-infobars")

        self.driver = webdriver.Chrome(options=self.chrome_options)
        try:
            self.driver.get(GAME_URL)
        except WebDriverException:
            pass

        # Wait for the game to load completely
        time.sleep(3)

    def start_game(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SPACE)

    def jump(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_UP)

    def duck(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)

    def get_screenshot(self):
        self.driver.save_screenshot("dino_game.png")

    def get_canvas_screenshot(self):
        canvas = self.driver.find_element(By.CLASS_NAME, "runner-canvas")
        canvas.screenshot("dino_game.png")

    def close(self):
        self.driver.quit()
