import pygame
from src.UI.UI_componenets import *
from src.data.settings import *
from src.data.map_arrays import map1

MENU_TEXT_COLOR = (150, 0, 0)
BUTTON_COLOR = (0, 125, 125)

def toggle_menu(panel, secondary_panel=None):
    panel.active = not panel.active
    if secondary_panel is not None:
        secondary_panel.active = not secondary_panel.active

def create_main_menu(game):
    from src.game_management.scene import LevelScene
    pygame.init()

    menu_panel = UIPanel(
        x_p=0.5,
        y_p=0.5,
        width_p=0.4,
        height_p=0.5,
        color=(255, 255, 255, 25),
    )

    title = UILabel(
        x_p=0.5,
        y_p=0,
        text="ANALOG ABYSS",
        font_size=200,
        color=MENU_TEXT_COLOR
    )

    play_button = UIButton(
        x_p=0.5,
        y_p=0.35,
        width_p=0.15,
        height_p=0.1,
        text="Play",
        font_size=40,
        font_color=MENU_TEXT_COLOR,
        color=BUTTON_COLOR,
        func=lambda: game.load_scene(LevelScene(game, map1))
    )

    settings_panel = create_setting_panel(menu_panel)
    settings_button = UIButton(
        x_p=0.5,
        y_p=0.48,
        width_p=0.15,
        height_p=0.1,
        text="Settings",
        font_size=40,
        font_color=MENU_TEXT_COLOR,
        color=BUTTON_COLOR,
        func=lambda: toggle_menu(settings_panel, menu_panel)
    )

    quit_button = UIButton(
        x_p=0.5,
        y_p=0.61,
        width_p=0.15,
        height_p=0.1,
        text="Quit",
        font_size=40,
        font_color=MENU_TEXT_COLOR,
        color=BUTTON_COLOR,
        func=lambda: game.quit_game()
    )

    menu_panel.add_children([title, play_button, settings_button, quit_button])

    main_menu = UIPanel(
        x_p=0,
        y_p=0,
        width_p=1,
        height_p=1,
        children=[menu_panel, settings_panel]
    )

    return main_menu

def create_setting_panel(menu):
    
    settings_panel = UIPanel(
        x_p=0.5,
        y_p=0.5,
        width_p=0.4,
        height_p=0.6,
        color=(255, 255, 255, 25),
        active=False
    )

    close_button = UIButton(
        x_p=0,
        y_p=0,
        width_p=0.03,
        height_p=0.03,
        text="X",
        font_size=40,
        font_color=(255, 255, 255),
        color=(150, 0, 0),
        func=lambda: toggle_menu(settings_panel, menu)
    )

    title = UILabel(
        x_p=0.5,
        y_p=0,
        text="SETTINGS",
        font_size=100,
        color=MENU_TEXT_COLOR
    )

    settings_panel.add_children([title, close_button])

    return settings_panel

def create_pause_menu(game):
    from src.game_management.scene import UIScene

    pause_menu = UIPanel(
        x_p=0,
        y_p=0,
        width_p=1,
        height_p=1,
    )

    pause_panel = UIPanel(
        x_p=0.5,
        y_p=0.5,
        width_p=0.4,
        height_p=0.6,
        color=(255, 255, 255, 25),
        active=False
    )

    title = UILabel(
        x_p=0.5,
        y_p=0,
        text="Pause Menu",
        font_size=100,
        color=MENU_TEXT_COLOR
    )

    resume_button = UIButton(
        x_p=0.5,
        y_p=0.38,
        width_p=0.15,
        height_p=0.1,
        text="Resume",
        font_size=40,
        font_color=MENU_TEXT_COLOR,
        color=BUTTON_COLOR,
        func=lambda: toggle_menu(pause_panel)
    )

    settings_panel = create_setting_panel(pause_panel)
    settings_button = UIButton(
        x_p=0.5,
        y_p=0.5,
        width_p=0.15,
        height_p=0.1,
        text="Settings",
        font_size=40,
        font_color=MENU_TEXT_COLOR,
        color=BUTTON_COLOR,
        func=lambda: toggle_menu(settings_panel, pause_panel)
    )

    main_menu_button = UIButton(
        x_p=0.5,
        y_p=0.62,
        width_p=0.15,
        height_p=0.1,
        text="Main Menu",
        font_size=40,
        font_color=MENU_TEXT_COLOR,
        color=BUTTON_COLOR,
        func=lambda: game.load_scene(UIScene(game, create_main_menu(game)))
    )

    pause_panel.add_children([title, resume_button, settings_button, main_menu_button])

    pause_menu.add_children([pause_panel, settings_panel])

    return pause_menu