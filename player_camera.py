import pygame
from raycasting import RayCasting
from settings import *
from lighting import Lighting

class PlayerCamera:
    def __init__(self, game, player):
        self.game = game
        self.player = player

    def ray_cast(self):

        curr_ray_angle = self.player.player_angle - (FOV / 2) + 0.0001

        for ray in range(RAY_AMT):
            ray_info = RayCasting.cast_ray(self.player.pos, self.player.map_pos, curr_ray_angle, MAX_DEPTH, self.game.map.map_dic)

            if ray_info[0]:

                corrected_ray_depth = ray_info[1] * math.cos(self.player.player_angle - curr_ray_angle)
                projection_height = SCREEN_DISTANCE / corrected_ray_depth

                projection_height = min(projection_height, HEIGHT)

                darkness_multiplier = 0.7

                distance_multiplier = (1 - ray_info[1] / MAX_DEPTH)

                projection_height_segments = projection_height / LIGHT_SEG_SIZE

                color = (255, 255, 255)

                center = (WIDTH // 2, HEIGHT //2)

                for segment in range(int(projection_height_segments)):

                    location = (ray * RAY_WIDTH_SCALE, ((HEIGHT - projection_height) // 2) + segment * LIGHT_SEG_SIZE)
    
                    color = Lighting.calculate_lighting_multiplier_flashlight((255, 255, 255), ray_info[1], location)

                    pygame.draw.rect(
                        self.game.screen,
                        color,
                        (ray * RAY_WIDTH_SCALE, ((HEIGHT - projection_height) // 2) + segment * LIGHT_SEG_SIZE, RAY_WIDTH_SCALE, LIGHT_SEG_SIZE)
                    )
                    
                pygame.draw.rect(
                    self.game.screen,
                    color,
                    (ray * RAY_WIDTH_SCALE, ((HEIGHT - projection_height) // 2) + (LIGHT_SEG_SIZE * int(projection_height_segments)), RAY_WIDTH_SCALE,  ((projection_height_segments) - int(projection_height_segments)) * LIGHT_SEG_SIZE)
                )


                #pygame.draw.line(
                #    self.game.screen, 
                #    'yellow', 
                #    (100 * self.player.pos[0], 100 * self.player.pos[1]),
                #    (100 * self.player.pos[0] + 100 * ray_depth * math.cos(curr_ray_angle), 100 * self.player.pos[1] + 100 * ray_depth * math.sin(curr_ray_angle)),
                #    2
                #    )

            curr_ray_angle += RAY_DELTA_ANGLE