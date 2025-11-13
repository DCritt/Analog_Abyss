import pygame
from player import Player
from player_camera import PlayerCamera
from map_arrays import *
from map import Map

#Base Class
class Scene:
    def __init__(self, game):
        self.game = game

    def update(self):
        pass

    def check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
                self.game.graphics_lib.free_map()
                self.game.graphics_lib.free_textures()

            self.check_event(event)

    def check_event(self, event):
        pass

    def draw(self):
        pass

#Child Classes
class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        super().update()

    def check_events(self, events):
        super().check_events(events)

    def draw(self):
        super().draw()

class Factory(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.map = Map(self, map1, self.game.graphics_lib)
        self.player = Player(self)
        self.player_camera = PlayerCamera(self.game, self.player)

    def update(self):
        super().update()
        self.player.update()

    def check_events(self, events):
        super().check_events(events)

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.player.event_update(event)

    def draw(self):
        super().draw()
        self.player_camera.draw_view()
