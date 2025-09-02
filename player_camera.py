import pygame
from raycasting import RayCasting
from settings import *
from concurrent.futures import ProcessPoolExecutor

class PlayerCamera:
    def __init__(self, game, player):
        self.game = game
        self.player = player

    def ray_cast(self):

        curr_ray_angle = self.player.player_angle - (FOV / 2) + 0.0001

        floor_segments = (HEIGHT // 2) / LIGHT_SEG_SIZE

        for segment in range(int(floor_segments)):
            floor_height_pixels = (HEIGHT // 2) + (segment * LIGHT_SEG_SIZE)
            floor_segment_dist = (0.5 * SCREEN_DISTANCE) / ((floor_height_pixels - (HEIGHT // 2)) + 0.00001)

            darkness_multiplier = 0.7

            distance_multiplier = (1 - min(floor_segment_dist, MAX_DEPTH) / MAX_DEPTH)

            center = (WIDTH // 2, HEIGHT //2)
            location = (WIDTH // 2, floor_height_pixels)
            distance = math.dist(center, location)

            flashlight_multiplier = (max(((1 / darkness_multiplier) * ((1 / max(distance_multiplier, 0.5)))) * (max(0, 1 - (distance / (HEIGHT * .75)))), darkness_multiplier))

            color = [255 * (darkness_multiplier * flashlight_multiplier * distance_multiplier)] * 3

            print(floor_segment_dist, color)

            pygame.draw.rect(self.game.screen, color, (0, floor_height_pixels, WIDTH, LIGHT_SEG_SIZE))

        for ray in range(RAY_AMT):
            ray_info = RayCasting.cast_ray(self.player.pos, self.player.map_pos, curr_ray_angle, MAX_DEPTH, self.game.map.map_dic)

            if ray_info[0]:

                corrected_ray_depth = ray_info[1] * math.cos(self.player.player_angle - curr_ray_angle)
                projection_height = SCREEN_DISTANCE / corrected_ray_depth

                projection_height = min(projection_height, HEIGHT)

                darkness_multiplier = 0.7

                distance_multiplier = (1 - ray_info[1] / MAX_DEPTH)
                
                #LIGHT_SEG_SIZE = int(projection_height / 8)

                projection_height_segments = projection_height / LIGHT_SEG_SIZE

                color = (0, 0, 0)

                center = (WIDTH // 2, HEIGHT //2)

                for segment in range(int(projection_height_segments)):

                    # dist_from_center_screen_hor = abs((ray * RAY_WIDTH_SCALE) - (WIDTH // 2))
                    # flash_light_multiplier_hor = 1 + (3 * (1 - (dist_from_center_screen_hor / (WIDTH // 2))))

                    # dist_from_center_screen_vert = abs((((HEIGHT - projection_height) // 2) + (segment * 8)) - (HEIGHT // 2))
                    # flash_light_multiplier_vert = 1 + (3 * (1 - (dist_from_center_screen_vert / (HEIGHT // 2))))

                    location = (ray * RAY_WIDTH_SCALE, ((HEIGHT - projection_height) // 2) + segment * LIGHT_SEG_SIZE)
                    distance = math.dist(center, location)

                    flashlight_multiplier = (max(((1 / darkness_multiplier) * ((1 / max(distance_multiplier, 0.5)))) * (max(0, 1 - (distance / (HEIGHT * .75)))), darkness_multiplier))

                    color = [255 * (darkness_multiplier * flashlight_multiplier * distance_multiplier)] * 3

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