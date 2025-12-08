from src.UI.UI_components.UI_componenets import *
from src.UI.UI_settings import MENU_TEXT_COLOR, BUTTON_COLOR
from src.data.map_arrays import map1

def build_main_menu_panel(game, toggle_settings_func):
    from src.game_management.scene import LevelScene

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
        func=lambda: game.load_scene(LevelScene(game, map1, "ambient"))
    )
    settings_button = UIButton(
        x_p=0.5,
        y_p=0.48,
        width_p=0.15,
        height_p=0.1,
        text="Settings",
        font_size=40,
        font_color=MENU_TEXT_COLOR,
        color=BUTTON_COLOR,
        func=toggle_settings_func
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
        func=game.quit_game
    )

    return UIPanel(
        x_p=0.5,
        y_p=0.5,
        width_p=0.4,
        height_p=0.5,
        color=(255, 255, 255, 25),
        children=[title, play_button, settings_button, quit_button]
    )