import pygame
from src.UI.UI_componenets import *
from src.data.settings import *
from src.data.map_arrays import map1
from src.game_management.scene import LevelScene

def create_main_menu(game):
    pygame.init()

    title_font = pygame.font.Font(None, 72)
    normal_font = pygame.font.Font(None, 40)

    main_menu = UIPanel(0, 0, WIDTH, HEIGHT, None)

    title_x = 0
    title_y = 0
    title_text = "ANALOG ABYSS"
    title_color = (150, 0, 0)
    title = UILabel(title_x, title_y, main_menu, title_text, title_font, title_color)

    play_button_text = "Play"

    play_button = UIButton(0, 100, 60, 30, main_menu, play_button_text, normal_font, title_color, (50, 50, 50), lambda: game.load_scene(LevelScene(game, map1)))

    main_menu.add_child(title)
    main_menu.add_child(play_button)

    return main_menu