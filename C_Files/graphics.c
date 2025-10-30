#include "graphics.h"

const Color WALL_COLOR = {46, 32, 25};
const Color CEIL_COLOR = {100, 100, 100};
const Color FLOOR_COLOR = {100, 100, 100};

int WIDTH;
int HEIGHT;

int RAY_AMT;
int LIGHT_SEG_SIZE;
double RAY_DELTA_ANGLE;
int RAY_WIDTH_SCALE;
double SCREEN_DISTANCE;

void init_graphics_settings(int width, int height, int definition) {
    WIDTH = width;
    HEIGHT = height;

    RAY_AMT = width / definition;
    LIGHT_SEG_SIZE = definition;
    RAY_DELTA_ANGLE = FOV / RAY_AMT;
    RAY_WIDTH_SCALE = width / RAY_AMT;
    SCREEN_DISTANCE = (width / 2) / tan(FOV / 2);
}

uint8_t* generate_pixels(const double player_pos[2], const int player_map_pos[2], const double player_angle) {
    
    Point pos = {player_pos[0], player_pos[1]};
    IntPoint map_pos = {player_map_pos[0], player_map_pos[1]};
    Point center_screen = {(WIDTH / 2), (HEIGHT / 2)};

    double curr_ray_angle = player_angle - (FOV / 2) + 0.0001;

    uint8_t* pixels = malloc(WIDTH * HEIGHT * 3);
    memset(pixels, 0, WIDTH * HEIGHT * 3);

    for (int i = 0; i < RAY_AMT; i++) {
        Ray ray = cast_ray(&pos, &map_pos, curr_ray_angle, MAX_DEPTH);
        
        if (ray.hit) {
            double corrected_ray_depth = ray.depth * cos(player_angle - curr_ray_angle);
            double projection_height = SCREEN_DISTANCE / (corrected_ray_depth + 0.000001);
            projection_height = (projection_height <= HEIGHT) ? projection_height : HEIGHT;

            int wall_segments = (int)projection_height / LIGHT_SEG_SIZE;

            int ray_offset = i * RAY_WIDTH_SCALE;
            int projection_height_offset = (int)((HEIGHT - projection_height) / 2);

            write_wall_slice(pixels, center_screen, wall_segments, ray_offset, projection_height, corrected_ray_depth);
            write_flat_slice(pixels, FLOOR_COLOR, center_screen, ray_offset, (int)(projection_height_offset + projection_height), (HEIGHT - 1));
            write_flat_slice(pixels, CEIL_COLOR, center_screen, ray_offset, 0, projection_height_offset);
        }
        curr_ray_angle += RAY_DELTA_ANGLE;
    }

    return pixels;

}

static inline void write_wall_slice(uint8_t *pixels, Point center_screen, int segments, int ray_offset, double proj_height, double ray_depth) {
    int proj_height_offset = (int)((HEIGHT - proj_height) / 2);

    int remainder_height = (int)(proj_height - (segments * LIGHT_SEG_SIZE));
    int total_segments = segments + (remainder_height > 0);
    for (int i = 0; i < total_segments; i++) {
        int segment_height = (i == segments) ? remainder_height : LIGHT_SEG_SIZE;
        int segment_offset = proj_height_offset + (i * LIGHT_SEG_SIZE);

        double center_screen_dist = (pow((ray_offset - center_screen.x), 2) + pow((segment_offset - center_screen.y), 2));
        double light_mult = lighting_multiplier_func(0.1, center_screen_dist, ray_depth, MAX_LIGHT_DISTANCE);
        
        uint8_t row[RAY_WIDTH_SCALE* 3];
        Color wall_color_lighted = {(WALL_COLOR.r * light_mult), (WALL_COLOR.g * light_mult), (WALL_COLOR.b * light_mult)};
        for (int j = 0; j < RAY_WIDTH_SCALE; j++) {
            row[(j * 3)] = wall_color_lighted.r;
            row[(j * 3) + 1] = wall_color_lighted.g;
            row[(j * 3) + 2] = wall_color_lighted.b;
        }

        int bit_offset = ((segment_offset * WIDTH) + ray_offset) * 3;
        for (int j = 0; j < segment_height; j++) {
            memcpy(((pixels + bit_offset) + (j * WIDTH * 3)), row, (RAY_WIDTH_SCALE * 3));
        }
    }
}

static inline void write_flat_slice(uint8_t *pixels, Color color, Point center_screen, int ray_offset, int y1, int y2) {
    int flat_height = y2 - y1;
    int dist_from_horizon = (y1 > center_screen.y) ? (y1 - center_screen.y) : (center_screen.y - y1);

    int segments = flat_height / LIGHT_SEG_SIZE;
    int remainder_height = flat_height - (segments * LIGHT_SEG_SIZE);
    int total_segments = segments + (remainder_height > 0);
    for (int i = 0; i < total_segments; i++) {
        int segment_height = (i == segments) ? remainder_height : LIGHT_SEG_SIZE;
        int segment_offset = y1 + (i * LIGHT_SEG_SIZE);

        double floor_dist = (dist_from_horizon == 0) ? INFINITY : ((CAMERA_HEIGHT * SCREEN_DISTANCE) / dist_from_horizon);
        double center_screen_dist = (pow((ray_offset - center_screen.x), 2) + pow((segment_offset - center_screen.y), 2));
        double light_mult = lighting_multiplier_func(0.1, center_screen_dist, floor_dist, MAX_LIGHT_DISTANCE);
    
        uint8_t row[RAY_WIDTH_SCALE * 3];
        Color color_lighted = {(color.r * light_mult), (color.g * light_mult), (color.b * light_mult)};
        for (int j = 0; j < RAY_WIDTH_SCALE; j++) {
            row[(j * 3)] = color_lighted.r;
            row[(j * 3) + 1] = color_lighted.g;
            row[(j * 3) + 2] = color_lighted.b;
        }

        int bit_offset = ((segment_offset * WIDTH) + ray_offset) * 3;
        for (int j = 0; j < segment_height; j++) {
            memcpy(((pixels + bit_offset) + (j * WIDTH * 3)), row, (RAY_WIDTH_SCALE * 3));
        }
        dist_from_horizon += (y1 > center_screen.y) ? segment_height : -segment_height;
    }
}