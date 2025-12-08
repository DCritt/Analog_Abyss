import pygame
from src.UI.UI_components.UI_componenets import UIPanel

class UI:
    def __init__(self, game, x_p, y_p, width_p, height_p):
        self.game = game
        self.root_panel = UIPanel(x_p, y_p, width_p, height_p)
        self.active = True

    def draw(self, surface):
        if not self.active:
            return
        self._draw(surface)

    def _draw(self, surface):
        self.root_panel.draw(surface)

    def update(self):
        if not self.active:
            return
        self._update()

    def _update(self):
        self.root_panel.update()
    
    def check_event(self, event):
        if not self.active:
            return False
        return self._check_event(event)
    
    def _check_event(self, event):
        self.root_panel.check_event(event)