import pygame
from src.game_management.game_manager import GameManager
from src.game_management.scene import UIScene, LevelScene
from src.data.map_arrays import map1
from src.UI.UI_componenets import UIPanel, UILabel, UIButton
from src.data.UI_scenes import create_main_menu

def button_func():
    print("worked")

if __name__ == '__main__':
    pygame.init()

    game = GameManager()
    menu = create_main_menu(game)
    game.load_scene(UIScene(game, menu))
    game.run()