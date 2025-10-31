import pygame
import ctypes
import numpy as np
from settings import *

class PlayerCamera:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.lib = game.graphics_lib

    def draw_view(self):

        player_pos = (ctypes.c_double * 2)(self.player.x, self.player.y)
        player_map_pos = (ctypes.c_int * 2)(self.player.map_pos[0], self.player.map_pos[1])

        pixels = self.lib.generate_pixels(player_pos, player_map_pos, self.player.player_angle)
        converted_pixels = np.ctypeslib.as_array(pixels, shape=(HEIGHT, WIDTH, 3))
        converted_pixels = np.transpose(converted_pixels, (1, 0, 2))

        pygame.surfarray.blit_array(self.game.screen, converted_pixels)
        self.lib.free_pixels(pixels)