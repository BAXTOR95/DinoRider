# DinoRider

DinoRider is a Python project that automates playing the Chrome Dino game using Selenium WebDriver. The bot can detect obstacles in the game and perform actions to avoid them, such as jumping and ducking.

## Project Structure

    ```
    DinoRider/
    ├── dino_game/
    │   ├── __init__.py
    │   ├── game.py
    │   ├── bot.py
    │   ├── config.py
    └── main.py
    ```

- **dino_game/**: Directory containing the main game and bot logic.
  - \***\*init**.py\*\*: Initializes the package.
  - **game.py**: Contains the `DinoGame` class that handles interactions with the Chrome Dino game.
  - **bot.py**: Contains the `DinoBot` class that implements the bot logic for playing the game.
  - **config.py**: Configuration file with game URL.
- **main.py**: Entry point of the project that initializes the game and bot, and starts the bot.

## Installation

### Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver compatible with your version of Chrome

### Setup

1. Clone the repository:

        ```bash
        git clone https://github.com/BAXTOR95/DinoRider.git
        cd DinoRider
        ```

2. Install the required Python packages:

        ```bash
        pip install -r requirements.txt
        ```

3. Ensure that ChromeDriver is installed and added to your system PATH. You can download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Usage

1. Run the `main.py` script:

        ```bash
        python main.py
        ```

2. The bot will automatically start the game and begin playing by detecting obstacles and performing actions to avoid them.

## Files Description

### `config.py`

Defines the URL of the Chrome Dino game.

    ```python
    GAME_URL = 'chrome://dino'
    ```

### `game.py`

Contains the `DinoGame` class that manages interactions with the game using Selenium.

### `bot.py`

Contains the `DinoBot` class that implements the logic for playing the game by capturing screenshots, detecting obstacles, and performing actions like jumping and ducking.

### `main.py`

Entry point of the project. Initializes the game and bot, and starts the bot.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more details.
