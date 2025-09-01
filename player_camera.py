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
            ray_depth = RayCasting.cast_ray(self.player.pos, self.player.map_pos, curr_ray_angle, MAX_DEPTH, self.game.map.map_dic)

            color = [255 * (1 - ray_depth / MAX_DEPTH)] * 3

            ray_depth *= math.cos(self.player.player_angle - curr_ray_angle)
            projection_height = SCREEN_DISTANCE / ray_depth

            pygame.draw.rect(
                self.game.screen,
                color,
                (ray * RAY_WIDTH_SCALE, (HEIGHT - projection_height) // 2, RAY_WIDTH_SCALE, projection_height)
                )

            #pygame.draw.line(
            #    self.game.screen, 
            #    'yellow', 
            #    (100 * self.player.pos[0], 100 * self.player.pos[1]),
            #    (100 * self.player.pos[0] + 100 * ray_depth * math.cos(curr_ray_angle), 100 * self.player.pos[1] + 100 * ray_depth * math.sin(curr_ray_angle)),
            #    2
            #    )

            curr_ray_angle += RAY_DELTA_ANGLE