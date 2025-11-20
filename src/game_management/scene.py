import pygame
from src.entities.player_files.player import Player
from src.game_management.camera import Camera
from src.data.map_arrays import *
from src.game_management.map import Map
from src.data.settings import *
from src.data.UI_elements import create_pause_menu

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
        self.pause_menu = create_pause_menu(game)

    def update(self):
        super().update()
        self.player.update()
        self.pause_menu.safe_update()

    def check_event(self, event):
        super().check_event(event)
        self.pause_menu.safe_check_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause_menu.children[0].active = not self.pause_menu.children[0].active
            self.player.event_update(event)

    def draw(self):
        super().draw()
        self.camera.draw_view()
        self.pause_menu.safe_draw(self.game.screen)

class UIScene(Scene):
    def __init__(self, game, ui):
        super().__init__(game)
        self.ui = ui

    def update(self):
        super().update()
        self.ui.safe_update()

    def check_event(self, event):
        super().check_event(event)
        self.ui.safe_check_event(event)

    def draw(self):
        super().draw()
        self.ui.safe_draw(self.game.screen)