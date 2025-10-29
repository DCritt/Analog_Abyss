#include "graphics.h"

void generate_pixels(uint8_t** pixels, const double player_pos[2], const int player_map_pos[2], const double player_angle, const uint8_t** map) {
    Point pos;
    pos.x = player_pos[0];
    pos.y = player_pos[1];

    IntPoint map_pos;
    map_pos.x = player_map_pos[0];
    map_pos.y = player_map_pos[1];

    double curr_ray_angle = player_angle;

    int i = 0;
    for (i = 0; i < RAY_AMT; i++) {
        Ray ray = cast_ray(&pos, &map_pos, player_angle, MAX_DEPTH, map);
        
        if (ray.hit) {
            double corrected_ray_depth = ray.depth * cos(player_angle - curr_ray_angle);
            double projection_height = SCREEN_DISTANCE / corrected_ray_depth;
            projection_height = (projection_height <= HEIGHT) ? projection_height : HEIGHT;

            double projection_height_segments = projection_height / LIGHT_SEG_SIZE;
            int projection_height_segments_int = (int)projection_height_segments;

            int ray_offset = i * RAY_WIDTH_SCALE;
            int projection_height_offset = (int)((HEIGHT - projection_height) / 2)

            int j = 0;
            for (j = 0; j < projection_height_segments_int; j++) {
                int segment_offset = j * LIGHT_SEG_SIZE;

                Point location;
                location.x = ray_offset;
                location.y = segment_offset + projection_height_offset;
            }
            
        }
        curr_ray_angle += RAY_DELTA_ANGLE;
    }

}