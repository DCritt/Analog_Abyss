import pygame
from src.entities.player_files.player import Player
from src.game_management.camera import Camera
from src.data.map_arrays import *
from src.game_management.map import Map

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
        player_pos = (1.5, 1.5)
        self.player = Player(self, player_pos)
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                self.game.load_scene(LevelScene(self.game, map1))

    def draw(self):
        super().draw()