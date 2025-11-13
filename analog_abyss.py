from Game import Game
from Scene import *

if __name__ == '__main__':
    game = Game()
    game.load_scene(MainMenu(game))
    game.run()