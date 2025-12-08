#ifndef TEXTURES_H
#define TEXTURES_H

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define COLOR_SIZE (3)

extern int WALL_TEX_DIMENSIONS;
extern int NUM_TEX;

extern uint8_t **wall_textures;

void init_textures(const char **file_paths, int num_paths, int dimensions);
void free_textures();
inline void get_tex_color(uint8_t out_color[COLOR_SIZE], int tex_num, int y, int x) {
    int bit_offset = ((y * WALL_TEX_DIMENSIONS) + x) * COLOR_SIZE;
    tex_num -= 1;
    out_color[0] = wall_textures[tex_num][bit_offset];
    out_color[1] = wall_textures[tex_num][bit_offset + 1];
    out_color[2] = wall_textures[tex_num][bit_offset + 2];
}

#endif