import pygame
from src.game_management.game_manager import GameManager
from src.game_management.scene import UIScene, LevelScene
from src.data.map_arrays import map1
from src.UI.UI_screens.main_menu import MainMenu

if __name__ == '__main__':
    pygame.init()

    game = GameManager()
    menu = MainMenu(game)
    game.load_scene(UIScene(game, menu, "oleum"))
    game.run()