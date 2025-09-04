from settings import *
from raycasting import RayCasting
from lighting import Lighting

MAP_DIC = None

def worker_init(map_dic):
    global MAP_DIC
    MAP_DIC = map_dic

def ray_cast_work(args):
        player_pos, player_map_pos, max_depth, player_angle, ray_delta_angle, ray_amt, starting_angle, ray_offset_start = args

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

        curr_ray_angle = starting_angle

        ray_rects = []

        for ray in range(int(ray_amt)):

            ray_info = RayCasting.cast_ray(player_pos, player_map_pos, curr_ray_angle, max_depth, MAP_DIC)

            if ray_info[0]:

                corrected_ray_depth = ray_info[1] * math.cos(player_angle - curr_ray_angle)
                projection_height = screen_distance / corrected_ray_depth
                projection_height = projection_height if projection_height <= height else height

                distance_multiplier = 0 if ray_info[1] > max_light_distance else 1 - (ray_info[1] * inverse_max_light_distance)

                projection_height_segments = projection_height / light_seg_size
                projection_height_segments_int = int(projection_height_segments)

                ray_offset = (ray * ray_width_scale) + ray_offset_start
                projection_height_offset = ((height - projection_height) // 2)

                color = (255, 255, 255)

                for segment in range(projection_height_segments_int):

                    segment_offset = segment * light_seg_size

                    location = (ray_offset, (projection_height_offset + segment_offset))
                    center_screen_distance = (location[0] - screen_center[0])**2 + (location[1] - screen_center[1])**2

                    #if center_screen_distance < max_flashlight_screen_distance: print(center_screen_distance, location, max_flashlight_screen_distance)

                    flashlight_multiplier = 1 if center_screen_distance > max_flashlight_screen_distance else Lighting.calculate_flashlight_multiplier(center_screen_distance, 1 / (distance_multiplier + 0.00001))

                    color = [255 * (darkness_multiplier * flashlight_multiplier * distance_multiplier)]*3

                    ray_rects.append(
                        (
                        color,
                        (ray_offset, (projection_height_offset + segment_offset), ray_width_scale, light_seg_size)
                        )
                    )
                    
                ray_rects.append(
                    (
                    color,
                    (ray_offset, (projection_height_offset + (light_seg_size * projection_height_segments_int)), ray_width_scale,  ((projection_height_segments) - projection_height_segments_int) * light_seg_size)
                    )
                )

            curr_ray_angle += ray_delta_angle

        return ray_rects