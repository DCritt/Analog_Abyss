#ifndef GRAPHICS_H
#define GRAPHICS_H

#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include "raycasting.h"
#include "lighting.h"
#include "textures.h"

#define FOV (M_PI / 3.0)
#define CAMERA_HEIGHT 0.5

extern int WIDTH;
extern int HEIGHT;

extern int RAY_AMT;
extern int LIGHT_SEG_SIZE;
extern double RAY_DELTA_ANGLE;
extern int RAY_WIDTH_SCALE;
extern int DEFINITION;
extern double SCREEN_DISTANCE;
extern Point CENTER_SCREEN;

extern double *flat_light_mults;

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

void init_graphics(int width, int height, int definition);
uint8_t* generate_pixels(const double player_pos[2], const int player_map_pos[2], double player_angle);
void free_pixels(uint8_t *pixels);

#endif