#include "map.h"

int map_width;
int map_height;

uint8_t **curr_map;

void set_map(int width, int height, uint8_t **map) {
    if (curr_map != NULL) { free(curr_map); }

    map_width = width;
    map_height = height;

    curr_map = malloc(height * sizeof(uint8_t *));
    for (int i = 0; i < height; i++) {
        curr_map[i] = malloc(width * sizeof(uint8_t));
        memcpy(curr_map[i], map[i], (width * sizeof(uint8_t)));
    }
}

void free_map() {
    for (int i = 0; i < map_height; i++) { free(curr_map[i]); }
    free(curr_map);
}