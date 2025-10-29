#ifndef LIGHTING_H
#define LIGHTING_H

#include "graphics.h"

#define MAX_LIGHT_DISTANCE (15)
#define MAX_FLASHLIGHT_SCREEN_DISTANCE (pow(((HEIGHT / 2) * 0.9), 2))
#define FLASHLIGHT_DISTANCE_NEGATION (0)
#define INVERSE_FLASHLIGHT_DISTANCE_NEGATION (1 / ((1 - FLASHLIGHT_DISTANCE_NEGATION) + 0.00001))

double calculate_lighting_multiplier(double dark_mult, double dist, double max_dist);

#endif