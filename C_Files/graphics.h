#ifndef GRAPHICS_H
#define GRAPHICS_H

#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include "raycasting.h"
#include "lighting.h"

#define FOV (M_PI / 3.0)
#define CAMERA_HEIGHT 0.5

extern int WIDTH;
extern int HEIGHT;

extern int RAY_AMT;
extern int LIGHT_SEG_SIZE;
extern double RAY_DELTA_ANGLE;
extern int RAY_WIDTH_SCALE;
extern double SCREEN_DISTANCE;

typedef struct Color {
    uint8_t r;
    uint8_t g;
    uint8_t b;
} Color;

typedef struct ColorA {
    uint8_t r;
    uint8_t g;
    uint8_t b;
    uint8_t a;
} ColorA;

void init_graphics_settings(int width, int height, int definition);
uint8_t* generate_pixels(const double player_pos[2], const int player_map_pos[2], double player_angle);
static inline void write_wall_slice(uint8_t *pixels, Point center_screen, int segments, int ray_offset, double proj_height, double ray_depth);
static inline void write_flat_slice(uint8_t *pixels, Color color, Point center_screen, int ray_offset, int y1, int y2);

#endif