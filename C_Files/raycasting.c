#include "raycasting.h"

Ray cast_ray(const Point *pos, const IntPoint *map_pos, const double angle, const double max_length, const uint8_t** map) {
    double radians = angle * (M_PI / 180);
    double sin_angle = sin(radians);
    double cos_angle = cos(radians);

    int hor_grid_coll_value = -1;
    IntPoint hor_map_pos;

    double hor_y = (sin_angle > 0) ? (map_pos->y) + 1 : (map_pos->y - 1e-6);
    int hor_dy = (sin_angle > 0) ? 1 : -1;

    double hor_depth = (hor_y - pos->y) / sin_angle;
    double hor_x = pos->x + (hor_depth * cos_angle);

    double hor_depth_delta = hor_dy / sin_angle;
    double hor_dx = hor_depth_delta * cos_angle;

    while (hor_depth < max_length) {
        hor_map_pos.x = (int)hor_x;
        hor_map_pos.y = (int)hor_y;
        if (map[hor_map_pos.x][hor_map_pos.y] != 0) {
            hor_grid_coll_value = map[hor_map_pos.x][hor_map_pos.y];
            break;         
        }
        hor_x += hor_dx;
        hor_y += hor_dy;
        hor_depth += hor_depth_delta;

        if (hor_depth > max_length) { hor_depth = max_length; }
    }

    int vert_grid_coll_value = -1;
    IntPoint vert_map_pos;

    double vert_x = (cos_angle > 0) ? (map_pos->x + 1) : (map_pos->x - 1e-6);
    int vert_dx = (cos_angle > 0) ? 1 : -1;

    double vert_depth = (vert_x - pos->x) / cos_angle;
    double vert_y = pos->y + (vert_depth * sin_angle);

    double vert_depth_delta = vert_dx / cos_angle;
    double vert_dy = vert_depth_delta * sin_angle;

    while (vert_depth < max_length) {
        vert_map_pos.x = (int)vert_x;
        vert_map_pos.y = (int)vert_y;
        if (map[vert_map_pos.x][vert_map_pos.y] != 0) {
            vert_grid_coll_value = map[vert_map_pos.x][vert_map_pos.y];
            break;         
        }
        vert_x += vert_dx;
        vert_y += vert_dy;
        vert_depth += vert_depth_delta;

        if (vert_depth > max_length) { vert_depth = max_length; }
    }

    Ray ray;
    if (hor_depth >= max_length && vert_depth >= max_length) {
        ray.hit = 0;
        ray.depth = -1;
        ray.hit_loc = NULL;
        ray.grid_val = -1;
        return ray;
    }

    ray.hit = 1;
    if (hor_depth <= vert_depth) {
        ray.depth = hor_depth;
        ray.hit_loc = hor_map_pos;
        ray.grid_val = hor_grid_coll_value;
    } else {
        ray.depth = vert_depth;
        ray.hit_loc = vert_map_pos;
        ray.grid_val = vert_grid_coll_value;
    }
    return ray;
}