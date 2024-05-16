import numpy as np
import time
from selenium.webdriver.common.by import By
from io import BytesIO
from PIL import Image


class DinoBot:
    """
    A class to represent the bot that plays the Chrome Dino game.

    Attributes:
    -----------
    game : DinoGame
        An instance of the DinoGame class to interact with the game.
    """

    def __init__(self, game):
        """
        Initialize the DinoBot with the game instance.

        Parameters:
        -----------
        game : DinoGame
            An instance of the DinoGame class.
        """
        self.game = game

    def get_game_screen(self):
        """
        Capture the current game screen.

        Returns:
        --------
        np.ndarray
            A grayscale image of the game screen as a numpy array.
        """
        screenshot = self.game.driver.get_screenshot_as_png()
        img = Image.open(BytesIO(screenshot))
        img = img.convert('L')  # Convert to grayscale
        img_np = np.array(img)
        return img_np

    def detect_obstacle(self, screen):
        """
        Detect obstacles in the game screen.

        Parameters:
        -----------
        screen : np.ndarray
            The current game screen as a numpy array.

        Returns:
        --------
        tuple
            A tuple containing two boolean values indicating the presence of ground and bird obstacles.
        """
        # Define the regions of interest for obstacle detection
        ground_roi = screen[225:250, 150:170]  # Region of interest for ground obstacles
        bird_roi = screen[165:190, 150:170]  # Region of interest for airborne obstacles

        # Thresholds based on observed values
        threshold = 20

        ground_obstacle = np.any(ground_roi < threshold)  # Check for ground obstacles
        bird_obstacle = np.any(bird_roi < threshold)  # Check for airborne obstacles

        return ground_obstacle, bird_obstacle

    def play(self):
        """Start playing the Chrome Dino game using the bot."""
        self.game.start_game()
        try:
            while True:
                screen = self.get_game_screen()
                ground_obstacle, bird_obstacle = self.detect_obstacle(screen)
                if bird_obstacle:
                    self.game.duck(0.5)  # Duck to avoid airborne obstacles
                elif ground_obstacle:
                    self.game.jump()  # Jump to avoid ground obstacles
                time.sleep(0.01)  # Short delay to prevent excessive CPU usage
        except KeyboardInterrupt:
            print("Game interrupted by user.")
            self.game.close()
