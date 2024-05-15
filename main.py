from dino_game.game import DinoGame
from dino_game.bot import DinoBot


def main():
    game = DinoGame()
    bot = DinoBot(game)
    try:
        bot.play()
    except KeyboardInterrupt:
        game.close()


if __name__ == "__main__":
    main()
