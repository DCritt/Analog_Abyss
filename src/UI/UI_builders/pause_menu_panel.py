from src.UI.UI_components.UI_componenets import *
from src.UI.UI_settings import MENU_TEXT_COLOR, BUTTON_COLOR
from src.UI.UI_screens.main_menu import MainMenu

def build_pause_menu_panel(game, toggle_settings_func, toggle_pause_menu_func):
    from src.game_management.scene import UIScene
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
        func=toggle_pause_menu_func
    )
    settings_button = UIButton(
        x_p=0.5,
        y_p=0.5,
        width_p=0.15,
        height_p=0.1,
        text="Settings",
        font_size=40,
        font_color=MENU_TEXT_COLOR,
        color=BUTTON_COLOR,
        func=toggle_settings_func
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
        func=lambda: game.load_scene(UIScene(game, MainMenu(game), "oleum"))
    )

    return UIPanel(
        x_p=0.5,
        y_p=0.5,
        width_p=0.4,
        height_p=0.6,
        color=(255, 255, 255, 25),
        children=[title, resume_button, settings_button, main_menu_button]
    )