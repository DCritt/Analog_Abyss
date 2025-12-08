import pygame
from src.UI.UI_components.UI_componenets import *
from src.UI.UI_settings import MENU_TEXT_COLOR, BUTTON_COLOR

def build_settings_panel(toggle_func):
    close_button = UIButton(
        x_p=0,
        y_p=0,
        width_p=0.03,
        height_p=0.03,
        text="X",
        font_size=40,
        font_color=(255, 255, 255),
        color=BUTTON_COLOR,
        func=toggle_func
    )
    title = UILabel(
        x_p=0.5,
        y_p=0,
        text="SETTINGS",
        font_size=100,
        color=MENU_TEXT_COLOR
    )

    return UIPanel(
        x_p=0.5,
        y_p=0.5,
        width_p=0.4,
        height_p=0.6,
        color=(255, 255, 255, 25),
        active=False,
        children=[title, close_button]
    )