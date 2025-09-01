import pygame
from map_arrays import _

class Map:
    def __init__(self, game, map_arr):
        self.game = game
        self.map_arr = map_arr
        self.map_dic = {}
        self.make_map_dic()

    def make_map_dic(self):
        for j, row in enumerate(self.map_arr):
            for i, value in enumerate(row):
                if value:
                    self.map_dic[(i, j)] = value

    def draw(self):
        for pos in self.map_dic:
            pygame.draw.rect(self.game.screen, (255, 0, 0), (pos[0] * 100, pos[1] * 100, 100, 100), 2)
