#ifndef MAP_H
#define MAP_H

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

extern int map_width;
extern int map_height;

extern uint8_t **curr_map;

void set_map(int width, int height, uint8_t **map);
void free_map();

#endif