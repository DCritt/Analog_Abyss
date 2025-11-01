#ifndef RAYCASTING_H
#define RAYCASTING_H

#include <math.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include "map.h"

#define MAX_DEPTH (30)

enum HitSide {
    TOP,
    BOTTOM,
    RIGHT,
    LEFT
};

typedef struct Point {
    double x;
    double y;
} Point;

typedef struct IntPoint {
    int x;
    int y;
} IntPoint;

typedef struct Ray {
    int hit;
    double depth;
    Point hit_loc;
    int grid_val;
    enum HitSide hit_side;
} Ray;

Ray cast_ray(const Point *pos, const IntPoint *map_pos, const double angle, const double max_length);

#endif