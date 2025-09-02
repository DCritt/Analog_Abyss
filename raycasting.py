from settings import *

class RayCasting:

    @staticmethod
    def cast_ray(pos, map_pos, angle, max_length, map_dic):
        sin_angle = math.sin(angle)
        cos_angle = math.cos(angle)

        #horizonal raycast
        hor_grid_coll_value = -1

        #determine which vertical direction the ray is going
        hor_y, hor_dy = (map_pos[1] + 1, 1) if sin_angle > 0 else (map_pos[1] - 1e-6, -1)

        #find inital depth and first y intercept x coordinate
        hor_depth = (hor_y - pos[1]) / sin_angle
        hor_x = pos[0] + hor_depth * cos_angle

        #find the depth delta of every y intecept jump and the delta x of every jump
        hor_depth_delta = hor_dy / sin_angle
        hor_dx = hor_depth_delta * cos_angle

        while (hor_depth < max_length):
            hor_map_pos = int(hor_x), int(hor_y)
            if (hor_map_pos in map_dic):
               hor_grid_coll_value = map_dic[hor_map_pos]
               break
            hor_x += hor_dx
            hor_y += hor_dy
            hor_depth += hor_depth_delta

            if (hor_depth > max_length):
               hor_depth = max_length

        #vertical raycast
        vert_grid_coll_value = -1

        #determine which vertical direction the ray is going
        vert_x, vert_dx = (map_pos[0] + 1, 1) if cos_angle > 0 else (map_pos[0] - 1e-6, -1)

        #find inital depth and first x intercept y coordinate
        vert_depth = (vert_x - pos[0]) / cos_angle
        vert_y = pos[1] + vert_depth * sin_angle

        #find the depth delta of every x intecept jump and the delta y of every jump
        vert_depth_delta = vert_dx / cos_angle
        vert_dy = vert_depth_delta * sin_angle

        while (vert_depth < max_length):
            vert_map_pos = int(vert_x), int(vert_y)
            if (vert_map_pos in map_dic):
                vert_grid_coll_value = map_dic[vert_map_pos]
                break
            vert_x += vert_dx
            vert_y += vert_dy
            vert_depth += vert_depth_delta

            if (vert_depth > max_length):
                vert_depth = max_length

        if (hor_depth == max_length and vert_depth == max_length):
            return (False, -1, None, -1)
        
        if (hor_depth <= vert_depth):
            return (True, hor_depth, (hor_x, hor_y), hor_grid_coll_value)
        else:
            return (True, vert_depth, (vert_x, vert_y), vert_grid_coll_value)