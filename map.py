import pygame
import ctypes
from map_arrays import _

class Map:
    def __init__(self, game, map_arr, lib):
        self.game = game
        self.map_arr = map_arr
        self.lib = lib
        self.map_dic = {}
        self.make_map_dic()
        
        c_map = self.convert_map()
        lib.set_map(len(map_arr), len(map_arr[0]), c_map)

    def convert_map(self):
        height = len(self.map_arr)
        width = len(self.map_arr[0])

        row_t = ctypes.c_uint8 * width
        rows = [row_t(*row) for row in self.map_arr]
        map_t = ctypes.POINTER(ctypes.c_uint8) * height
        map_ptr = map_t(*[ctypes.cast(row, ctypes.POINTER(ctypes.c_uint8)) for row in rows])

        return map_ptr

    def make_map_dic(self):
        for j, row in enumerate(self.map_arr):
            for i, value in enumerate(row):
                if value:
                    self.map_dic[(i, j)] = value

    def draw(self):
        for pos in self.map_dic:
            pygame.draw.rect(self.game.screen, (255, 0, 0), (pos[0] * 100, pos[1] * 100, 100, 100), 2)
