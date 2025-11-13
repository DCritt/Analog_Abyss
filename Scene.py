import pygame
from player import Player
from Camera import Camera
from map_arrays import *
from map import Map

#Base Class
class Scene:
    def __init__(self, game):
        self.game = game

    def update(self):
        pass

    def check_event(self, event):
        pass

    def draw(self):
        pass

#Child Classes
class LevelScene(Scene):
    def __init__(self, game, map):
        super().__init__(game)
        self.map = Map(game, map, game.graphics_lib)
        self.player = Player(self)
        self.camera = Camera(game, self.player)

    def update(self):
        super().update()
        self.player.update()

    def check_event(self, event):
        super().check_event(event)
        if event.type == pygame.KEYDOWN:
            self.player.event_update(event)

    def draw(self):
        super().draw()
        self.camera.draw_view()

class UIScene(Scene):
    def __init__(self, game, ui):
        super().__init__(game)
        self.ui = ui

    def update(self):
        super().update()

    def check_event(self, event):
        super().check_event(event)

    def draw(self):
        super().draw()