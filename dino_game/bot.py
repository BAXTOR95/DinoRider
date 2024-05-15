import time
import numpy as np
from selenium.webdriver.common.by import By
from io import BytesIO
from PIL import Image


class DinoBot:
    def __init__(self, game):
        self.game = game

    def get_game_screen(self):
        screenshot = self.game.driver.get_screenshot_as_png()
        # Save the screenshot to a file for debugging
        with open("screenshot.png", "wb") as f:
            f.write(screenshot)
        img = Image.open(BytesIO(screenshot))
        img = img.convert('L')  # Convert to grayscale
        img_np = np.array(img)
        return img_np

    def detect_obstacle(self, screen):
        # Define the regions of interest for obstacle detection
        ground_roi = screen[651:770, 320:394]  # Region of interest for ground obstacles
        Image.fromarray(ground_roi).save("ground_roi.png")

        bird_roi = screen[586:650, 320:394]  # Region of interest for airborne obstacles
        Image.fromarray(bird_roi).save("bird_roi.png")

        # Debug print statements
        print("Ground Region Mean Intensity:", np.mean(ground_roi))
        print("Bird Region Mean Intensity:", np.mean(bird_roi))

        # Adjusted threshold based on dark theme
        threshold = 33
        ground_obstacle = np.any(ground_roi < threshold)  # Check for ground obstacles
        bird_obstacle = np.any(bird_roi < threshold)  # Check for airborne obstacles

        # Save the regions of interest to files for debugging when an obstacle is detected
        if ground_obstacle:
            Image.fromarray(ground_roi).save("ground_obstacle.png")
        if bird_obstacle:
            Image.fromarray(bird_roi).save("bird_obstacle.png")

        return ground_obstacle, bird_obstacle

    def play(self):
        self.game.start_game()
        while True:
            screen = self.get_game_screen()
            ground_obstacle, bird_obstacle = self.detect_obstacle(screen)
            if bird_obstacle:
                print("Bird obstacle detected! Ducking!")
                self.game.duck()  # Duck to avoid airborne obstacles
            elif ground_obstacle:
                print("Ground obstacle detected! Jumping!")
                self.game.jump()  # Jump to avoid ground obstacles

            time.sleep(0.1)
