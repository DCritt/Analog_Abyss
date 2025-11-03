#include "graphics.h"

const Color CEIL_COLOR = {33, 44, 53};
const Color FLOOR_COLOR = {50, 50, 50};

int WIDTH;
int HEIGHT;

int RAY_AMT;
double RAY_DELTA_ANGLE;
int RAY_WIDTH_SCALE;
int DEFINITION;
double SCREEN_DISTANCE;
Point CENTER_SCREEN;

void init_graphics(int width, int height, int definition) {
    WIDTH = width;
    HEIGHT = height;

    RAY_AMT = width / definition;
    RAY_DELTA_ANGLE = FOV / RAY_AMT;
    RAY_WIDTH_SCALE = width / RAY_AMT;
    DEFINITION = definition;
    SCREEN_DISTANCE = (width / 2) / tan(FOV / 2);
    CENTER_SCREEN.x = width / 2;
    CENTER_SCREEN.y = height / 2;

}

static inline double get_flat_light_mult(int dist_from_horizon, int ray_offset) { 
    return flat_light_mults[(((int)(dist_from_horizon / DEFINITION)) * (WIDTH / DEFINITION)) + (int)(ray_offset / DEFINITION)]; 
}

static inline void write_wall_slice(uint8_t *pixels, int segments, int ray_offset, int proj_height, double ray_depth, int wall_tex_num, int ray_texture_offset) {
    int proj_height_offset = (int)((HEIGHT - proj_height) / 2);

    int remainder_height = (int)(proj_height - (segments * DEFINITION));
    int total_segments = segments + (remainder_height > 0);
    for (int i = 0; i < total_segments; i++) {
        int segment_height = (i == segments) ? remainder_height : DEFINITION;
        int segment_offset = proj_height_offset + (i * DEFINITION);

        double center_screen_dist = (pow((ray_offset - CENTER_SCREEN.x), 2) + pow((segment_offset - CENTER_SCREEN.y), 2));
        double light_mult = lighting_multiplier_func(center_screen_dist, ray_depth, MAX_LIGHT_DISTANCE);

        int texture_offset_y = round(((WALL_TEX_DIMENSIONS - 1) * ((i * DEFINITION) / (double)proj_height)));
        uint8_t color[COLOR_SIZE];
        get_tex_color(color, wall_tex_num, texture_offset_y, ray_texture_offset);
        uint8_t color_row[COLOR_SIZE * RAY_WIDTH_SCALE];
        color[0] = color[0] * light_mult;
        color[1] = color[1] * light_mult;
        color[2] = color[2] * light_mult;
        for (int j = 0; j < RAY_WIDTH_SCALE; j++) {
            color_row[(j * COLOR_SIZE)] = color[0];
            color_row[(j * COLOR_SIZE) + 1] = color[1];
            color_row[(j * COLOR_SIZE) + 2] = color[2];
        }

        int bit_offset = ((segment_offset * WIDTH) + ray_offset) * 3;
        for (int j = 0; j < segment_height; j++) {
            memcpy(((pixels + bit_offset) + (j * WIDTH * COLOR_SIZE)), color_row, (RAY_WIDTH_SCALE * COLOR_SIZE));
        }
    }
}

static inline void write_flat_slice(uint8_t *pixels, Color color, int ray_offset, int y1, int y2) {
    int flat_height = y2 - y1;
    int dist_from_horizon = (y1 > CENTER_SCREEN.y) ? (y1 - CENTER_SCREEN.y) : (CENTER_SCREEN.y - y1);

    int segments = flat_height / DEFINITION;
    int remainder_height = flat_height - (segments * DEFINITION);
    int total_segments = segments + (remainder_height > 0);
    for (int i = 0; i < total_segments; i++) {
        int segment_height = (i == segments) ? remainder_height : DEFINITION;
        int segment_offset = y1 + (i * DEFINITION);

        double floor_dist = (dist_from_horizon == 0) ? INFINITY : ((CAMERA_HEIGHT * SCREEN_DISTANCE) / dist_from_horizon);
        double center_screen_dist = (pow((ray_offset - CENTER_SCREEN.x), 2) + pow(dist_from_horizon, 2));
        double light_mult = lighting_multiplier_func(center_screen_dist, floor_dist, MAX_LIGHT_DISTANCE);

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
        dist_from_horizon += (y1 > CENTER_SCREEN.y) ? segment_height : -segment_height;
    }
}

uint8_t* generate_pixels(const double player_pos[2], const int player_map_pos[2], const double player_angle) {
    
    Point pos = {player_pos[0], player_pos[1]};
    IntPoint map_pos = {player_map_pos[0], player_map_pos[1]};

    double curr_ray_angle = player_angle - (FOV / 2) + 0.0001;

    uint8_t* pixels = malloc(WIDTH * HEIGHT * 3);
    memset(pixels, 0, WIDTH * HEIGHT * 3);

    for (int i = 0; i < RAY_AMT; i++) {
        Ray ray = cast_ray(&pos, &map_pos, curr_ray_angle, MAX_DEPTH);
        
        enum HitSide side = ray.hit_side;
        double hit_prop;
        if (side == TOP || side == BOTTOM) {
            hit_prop = ray.hit_loc.x - floor(ray.hit_loc.x);
        } else {
            hit_prop = ray.hit_loc.y - floor(ray.hit_loc.y);
        }

        if (side == TOP || side == RIGHT) {
            hit_prop = 1.0 - hit_prop;
        }

        int ray_texture_offset = round((WALL_TEX_DIMENSIONS - 1) * hit_prop);
        int ray_offset = i * RAY_WIDTH_SCALE;

        if (ray.hit) {
            double corrected_ray_depth = ray.depth * cos(player_angle - curr_ray_angle);
            int projection_height = (int)(SCREEN_DISTANCE / (corrected_ray_depth + 0.00001));
            projection_height = (projection_height <= HEIGHT) ? projection_height : HEIGHT;

            int wall_segments = (int)projection_height / DEFINITION;

            int projection_height_offset = (int)((HEIGHT - projection_height) / 2);

            write_wall_slice(pixels, wall_segments, ray_offset, projection_height, corrected_ray_depth, ray.grid_val, ray_texture_offset);
            write_flat_slice(pixels, FLOOR_COLOR, ray_offset, (int)(projection_height_offset + projection_height), (HEIGHT - 1));
            write_flat_slice(pixels, CEIL_COLOR, ray_offset, 0, projection_height_offset);
        } else {
            write_flat_slice(pixels, FLOOR_COLOR, ray_offset, (HEIGHT / 2), (HEIGHT - 1));
            write_flat_slice(pixels, CEIL_COLOR, ray_offset, 0, ((HEIGHT / 2) - 1));
        }
        curr_ray_angle += RAY_DELTA_ANGLE;
    }

    return pixels;

}

void free_pixels(uint8_t *pixels) { free(pixels); }