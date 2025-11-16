import pygame
import ctypes
import numpy as np
from src.data.settings import *

class Camera:
    def __init__(self, game, entity):
        self.game = game
        self.entity = entity
        self.lib = game.graphics_lib

    def draw_view(self):
        player_pos = (ctypes.c_double * 2)(self.entity.x, self.entity.y)
        player_map_pos = (ctypes.c_int * 2)(self.entity.map_pos[0], self.entity.map_pos[1])

        pixels = self.lib.generate_pixels(player_pos, player_map_pos, self.entity.angle)
        converted_pixels = np.ctypeslib.as_array(pixels, shape=(HEIGHT, WIDTH, 3))
        converted_pixels = np.transpose(converted_pixels, (1, 0, 2))

        pygame.surfarray.blit_array(self.game.screen, converted_pixels)
        self.lib.free_pixels(pixels)