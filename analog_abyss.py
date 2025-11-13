from Game import Game
from Scene import *
from map_arrays import map1

if __name__ == '__main__':
    game = Game()
    game.load_scene(LevelScene(game, map1))
    game.run()