#ifndef GRAPHICS_H
#define GRAPHICS_H

#include <stdint.h>
#include "raycasting.h"

#define WIDTH (1500)
#define HEIGHT (900)

#define FOV (M_PI / 3.0)
#define RAY_AMT (WIDTH / 12)
#define LIGHT_SEG_SIZE (12)
#define RAY_DELTA_ANGLE (FOV / RAY_AMT)
#define RAY_WIDTH_SCALE (WIDTH / RAY_AMT)
#define SCREEN_DISTANCE = ((WIDTH / 2) / tan(FOV / 2))

void generate_pixels(uint8_t** pixels, const double player_pos[2], const int player_map_pos[2], double player_angle, const uint8_t** map);

#endif