import pygame
from raycasting import RayCasting
from settings import *
from lighting import Lighting
from multiprocessing import Pool, cpu_count
from pool import *

class PlayerCamera:
    def __init__(self, game, player):
        self.game = game
        self.player = player

    def ray_cast(self):

        ray_delta_angle = RAY_DELTA_ANGLE

        player_pos = self.player.pos
        player_map_pos = self.player.map_pos
        curr_ray_angle = self.player.player_angle - (FOV / 2) + 0.0001
        max_depth = MAX_DEPTH
        map_dic = self.game.map.map_dic

        cpu_amt = cpu_count()
        ray_amt_per_process = RAY_AMT / cpu_amt
        cpu_angle_delta = FOV / cpu_amt
        pixel_per_cpu = WIDTH / cpu_amt
        
        args = [(player_pos, player_map_pos, max_depth, self.player.player_angle, ray_delta_angle, ray_amt_per_process, (curr_ray_angle + (ray_segment * cpu_angle_delta)), pixel_per_cpu * ray_segment) for ray_segment in range(cpu_amt)]

        rects_to_draw = self.game.pool.map(ray_cast_work, args)

        for ray_rects in rects_to_draw:
            for rect in ray_rects:
                pygame.draw.rect(self.game.screen, rect[0], rect[1])

        # for ray in range(RAY_AMT):
        #     ray_info = RayCasting.cast_ray(player_pos, player_map_pos, curr_ray_angle, max_depth, map_dic)

        #     if ray_info[0]:

        #         corrected_ray_depth = ray_info[1] * math.cos(self.player.player_angle - curr_ray_angle)
        #         projection_height = screen_distance / corrected_ray_depth
        #         projection_height = projection_height if projection_height <= height else height

        #         distance_multiplier = 0 if ray_info[1] > max_light_distance else 1 - (ray_info[1] * inverse_max_light_distance)

        #         projection_height_segments = projection_height / light_seg_size
        #         projection_height_segments_int = int(projection_height_segments)

        #         ray_offset = ray * ray_width_scale
        #         projection_height_offset = ((height - projection_height) // 2)

        #         color = (255, 255, 255)

        #         for segment in range(projection_height_segments_int):

        #             segment_offset = segment * light_seg_size

        #             location = (ray_offset, (projection_height_offset + segment_offset))
        #             center_screen_distance = (location[0] - screen_center[0])**2 + (location[1] - screen_center[1])**2

        #             flashlight_multiplier = 1 if center_screen_distance > max_flashlight_screen_distance else Lighting.calculate_flashlight_multiplier(center_screen_distance, 1 / (distance_multiplier + 0.00001))
    
        #             color = [255 * (darkness_multiplier * flashlight_multiplier * distance_multiplier)]*3

        #             pygame.draw.rect(
        #                 self.game.screen,
        #                 color,
        #                 (ray_offset, (projection_height_offset + segment_offset), ray_width_scale, light_seg_size)
        #             )
                    
        #         pygame.draw.rect(
        #             self.game.screen,
        #             color,
        #             (ray_offset, (projection_height_offset + (light_seg_size * projection_height_segments_int)), ray_width_scale,  ((projection_height_segments) - projection_height_segments_int) * light_seg_size)
        #         )


        #         #pygame.draw.line(
        #         #    self.game.screen, 
        #         #    'yellow', 
        #         #    (100 * self.player.pos[0], 100 * self.player.pos[1]),
        #         #    (100 * self.player.pos[0] + 100 * ray_depth * math.cos(curr_ray_angle), 100 * self.player.pos[1] + 100 * ray_depth * math.sin(curr_ray_angle)),
        #         #    2
        #         #    )

        #     curr_ray_angle += ray_delta_angle