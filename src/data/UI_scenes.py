import pygame
from src.UI.UI_componenets import *
from src.data.settings import *
from src.data.map_arrays import map1
from src.game_management.scene import LevelScene

def create_main_menu(game):
    pygame.init()

    title_x = 0
    title_y = 0
    title_text = "ANALOG ABYSS"
    title_color = (150, 0, 0)
    title = UILabel(title_x, title_y, title_text, 72, title_color)

    play_button_text = "Play"
    play_button = UIButton(0, 0.1, 0.05, 0.07, play_button_text, 40, title_color, (50, 50, 50), lambda: game.load_scene(LevelScene(game, map1)))

    main_menu = UIPanel(0, 0, 1, 1, [title, play_button])
    main_menu.resize(0, 0, 0.5, 0.5)

    return main_menu