import pygame
from raycasting import RayCasting
from settings import *

class PlayerCamera:
    def __init__(self, game, player):
        self.game = game
        self.player = player

    def ray_cast(self):

        curr_ray_angle = self.player.player_angle - (FOV / 2) + 0.0001
        for ray in range(RAY_AMT):
            ray_depth = RayCasting.cast_ray(self.player.pos[0], self.player.pos[1], self.player.map_pos[0], self.player.map_pos[0], curr_ray_angle, MAX_DEPTH, self.game)
            pygame.draw.line(
                self.game.screen, 
                'yellow', 
                (100 * self.player.pos[0], 100 * self.player.pos[1]),
                (100 * self.player.pos[0] + 100 * ray_depth * math.cos(curr_ray_angle), 100 * self.player.pos[1] + 100 * ray_depth * math.sin(curr_ray_angle)),
                2
                )

            curr_ray_angle += RAY_DELTA_ANGLE