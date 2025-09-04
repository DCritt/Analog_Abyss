import pygame
from raycasting import RayCasting
from settings import *
from lighting import Lighting

class PlayerCamera:
    def __init__(self, game, player):
        self.game = game
        self.player = player

    def ray_cast(self):

        darkness_multiplier = DARKNESS_MULTIPLIER
        height = HEIGHT
        ray_width_scale = RAY_WIDTH_SCALE
        light_seg_size = LIGHT_SEG_SIZE
        ray_delta_angle = RAY_DELTA_ANGLE
        screen_distance = SCREEN_DISTANCE
        max_light_distance = MAX_LIGHT_DISTANCE
        inverse_max_light_distance = INVERSE_MAX_LIGHT_DISTANCE
        screen_center = SCREEN_CENTER
        max_flashlight_screen_distance = MAX_FLASHLIGHT_SCREEN_DISTANCE

        player_pos = self.player.pos
        player_map_pos = self.player.map_pos
        curr_ray_angle = self.player.player_angle - (FOV / 2) + 0.0001
        max_depth = MAX_DEPTH
        map_dic = self.game.map.map_dic

        camera_height = 0.5

        for ray in range(RAY_AMT):
            ray_info = RayCasting.cast_ray(player_pos, player_map_pos, curr_ray_angle, max_depth, map_dic)

            if ray_info[0]:

                corrected_ray_depth = ray_info[1] * math.cos(self.player.player_angle - curr_ray_angle)
                projection_height = screen_distance / corrected_ray_depth
                projection_height = projection_height if projection_height <= height else height

                distance_multiplier = 0 if ray_info[1] > max_light_distance else 1 - (ray_info[1] * inverse_max_light_distance)

                projection_height_segments = projection_height / light_seg_size
                projection_height_segments_int = int(projection_height_segments)

                ray_offset = ray * ray_width_scale
                projection_height_offset = ((height - projection_height) // 2)

                color = (255, 255, 255)

                for segment in range(projection_height_segments_int):

                    segment_offset = segment * light_seg_size

                    location = (ray_offset, (projection_height_offset + segment_offset))
                    center_screen_distance = (location[0] - screen_center[0])**2 + (location[1] - screen_center[1])**2

                    flashlight_multiplier = 1 if center_screen_distance > max_flashlight_screen_distance else Lighting.calculate_flashlight_multiplier(center_screen_distance, 1 / (distance_multiplier + 0.00001))
    
                    color = [255 * (darkness_multiplier * flashlight_multiplier * distance_multiplier)]*3

                    pygame.draw.rect(
                        self.game.screen,
                        color,
                        (location[0], location[1], ray_width_scale, light_seg_size)
                    )

                pygame.draw.rect(
                    self.game.screen,
                    color,
                    (ray_offset, (projection_height_offset + (light_seg_size * projection_height_segments_int)), ray_width_scale,  ((projection_height_segments) - projection_height_segments_int) * light_seg_size)
                )

                projection_offset = projection_height_offset + projection_height

                floor_segments = (HEIGHT - projection_offset) / light_seg_size
                floor_segments_int = int(floor_segments)

                for segment in range(floor_segments_int):
                    segment_height = projection_offset + (segment * light_seg_size)
                    height_from_horizon = segment_height - (height // 2)

                    floor_distance = float("inf") if height_from_horizon == 0 else (camera_height * screen_distance) / (height_from_horizon)
                    distance_multiplier = 0 if floor_distance > max_light_distance else 1 - (floor_distance * inverse_max_light_distance)
                    
                    center_screen_distance = (ray_offset - screen_center[0])**2 + (segment_height - screen_center[1])**2
                    flashlight_multiplier = 1 if center_screen_distance > max_flashlight_screen_distance else Lighting.calculate_flashlight_multiplier(center_screen_distance, 1 / (distance_multiplier + 0.00001))

                    color = [200 * (darkness_multiplier * flashlight_multiplier * distance_multiplier)]*3

                    pygame.draw.rect(
                        self.game.screen,
                        color,
                        (ray_offset, segment_height, ray_width_scale, light_seg_size)
                    )

                #pygame.draw.line(
                #    self.game.screen, 
                #    'yellow', 
                #    (100 * self.player.pos[0], 100 * self.player.pos[1]),
                #    (100 * self.player.pos[0] + 100 * ray_depth * math.cos(curr_ray_angle), 100 * self.player.pos[1] + 100 * ray_depth * math.sin(curr_ray_angle)),
                #    2
                #    )

            curr_ray_angle += ray_delta_angle