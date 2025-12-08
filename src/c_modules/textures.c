#include "textures.h"

int WALL_TEX_DIMENSIONS;
int NUM_TEX;

uint8_t **wall_textures;

void init_textures(const char **file_paths, int num_paths, int dimensions) {
    WALL_TEX_DIMENSIONS = dimensions;
    NUM_TEX = num_paths;
    wall_textures = malloc(num_paths * sizeof(uint8_t *));

    size_t size = dimensions * dimensions * COLOR_SIZE;

    for (int i = 0; i < num_paths; i++) {
        wall_textures[i] = malloc(size * sizeof(uint8_t));

        FILE *fp = fopen(file_paths[i], "rb");

        for (int j = 0; j < 3; j++) {
            while (fgetc(fp) != '\n');
        }

        fread(wall_textures[i], 1, size, fp);
        
        fclose(fp);
    }
}

void free_textures() {
    for (int i = 0; i < NUM_TEX; i++) {
        free(wall_textures[i]);
    }
    free(wall_textures);
}