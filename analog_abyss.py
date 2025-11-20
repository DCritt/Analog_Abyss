import pygame
from src.game_management.game_manager import GameManager
from src.game_management.scene import UIScene, LevelScene
from src.data.map_arrays import map1
from src.data.UI_elements import create_main_menu

if __name__ == '__main__':
    pygame.init()

    game = GameManager()
    menu = create_main_menu(game)
    game.load_scene(UIScene(game, menu))
    game.run()