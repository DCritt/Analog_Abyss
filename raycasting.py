from settings import *

class RayCasting:

    @staticmethod
    def cast_ray(x, y, map_x, map_y, angle, max_length, game):
        sin_angle = math.sin(angle)
        cos_angle = math.cos(angle)

        #horizonal raycast

        #determine which vertical direction the ray is going
        map_y = math.floor(y)
        hor_y, hor_dy = (map_y + 1, 1) if sin_angle > 0 else (map_y - 1e-6, -1)

        #find inital depth and first y intercept x coordinate
        hor_depth = (hor_y - y) / sin_angle
        hor_x = x + hor_depth * cos_angle

        #find the depth delta of every y intecept jump and the delta x of every jump
        hor_depth_delta = hor_dy / sin_angle
        hor_dx = hor_depth_delta * cos_angle

        while (hor_depth < max_length):
            hor_map_pos = int(hor_x), int(hor_y)
            if (hor_map_pos in game.map.map_dic):
               break
            hor_x += hor_dx
            hor_y += hor_dy
            hor_depth += hor_depth_delta

            if (hor_depth > max_length):
               hor_depth = max_length

        #vertical raycast

        #determine which vertical direction the ray is going
        vert_x, vert_dx = (map_x + 1, 1) if cos_angle > 0 else (map_x - 1e-6, -1)

        #find inital depth and first x intercept y coordinate
        vert_depth = (vert_x - x) / cos_angle
        vert_y = y + vert_depth * sin_angle

        #find the depth delta of every x intecept jump and the delta y of every jump
        vert_depth_delta = vert_dx / cos_angle
        vert_dy = vert_depth_delta * sin_angle

        while (vert_depth < max_length):
            vert_map_pos = int(vert_x), int(vert_y)
            if (vert_map_pos in game.map.map_dic):
                break
            vert_x += vert_dx
            vert_y += vert_dy
            vert_depth += vert_depth_delta

            if (vert_depth > max_length):
                vert_depth = max_length
        
        if (hor_depth <= vert_depth):
            return hor_depth
        else:
            return vert_depth