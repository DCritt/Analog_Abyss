import pygame
from src.UI.UI_componenets import *
from src.data.settings import *
from src.data.map_arrays import map1
from src.game_management.scene import LevelScene

def create_main_menu(game):
    pygame.init()

    title = UILabel(
        x_p=0,
        y_p=0,
        text="ANALOG ABYSS",
        font_size=200,
        color=(150, 0, 0)
    )

    play_button_text = "Play"
    play_button = UIButton(0.5, 0.35, 0.15, 0.1, play_button_text, 40, (150, 0, 0), (50, 50, 50), lambda: game.load_scene(LevelScene(game, map1)))

    menu_panel = UIPanel(
        x_p=0.5,
        y_p=0.5,
        width_p=0.4,
        height_p=0.5,
        children=[title, play_button]
    )

    main_menu = UIPanel(0, 0, 1, 1, [menu_panel])
    #main_menu.resize(0, 0, 0.1, 0.1)

    return main_menu