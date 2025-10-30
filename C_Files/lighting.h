#ifndef LIGHTING_H
#define LIGHTING_H

#include "graphics.h"

#define MAX_LIGHT_DISTANCE (15)
#define FLASHLIGHT_DISTANCE_NEGATION (0)
#define INVERSE_FLASHLIGHT_DISTANCE_NEGATION (1 / ((1 - FLASHLIGHT_DISTANCE_NEGATION) + 0.00001))

extern double max_flashlight_screen_distance;

extern double (*lighting_multiplier_func)(double, double, double, double);
extern int flashlight;

void init_lighting_settings(int height);
double calculate_lighting_multiplier_f(double dark_mult, double center_screen_dist, double dist, double max_dist);
double calculate_lighting_multiplier_nf(double dark_mult, double center_screen_dist, double dist, double max_dist);
void toggle_flashlight();

#endif