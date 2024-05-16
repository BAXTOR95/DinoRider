from dino_game.game import DinoGame
from dino_game.bot import DinoBot


def main():
    """
    Main function to initialize the game and bot, and start playing the game.
    """
    game = DinoGame()
    bot = DinoBot(game)
    try:
        bot.play()
    except KeyboardInterrupt:
        print("Game interrupted by user.")
        game.close()


if __name__ == "__main__":
    main()
