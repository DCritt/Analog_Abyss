#ifndef LIGHTING_H
#define LIGHTING_H

#include "graphics.h"

#define FLASHLIGHT_DISTANCE_NEGATION (0)
#define INVERSE_FLASHLIGHT_DISTANCE_NEGATION (1 / ((1 - FLASHLIGHT_DISTANCE_NEGATION) + 0.00001))

extern double MAX_FLASHLIGHT_SCREEN_DISTANCE;
extern double darkness_multiplier;
extern double max_light_distance;

extern double (*lighting_multiplier_func)(double, double);
extern int flashlight;

void init_lighting_settings(int height, double dark_mult, double max_light_dist);
void set_darkness(double dark_mult, double max_light_dist);
double calculate_lighting_multiplier_f(double center_screen_dist, double dist);
double calculate_lighting_multiplier_nf(double center_screen_dist, double dist);
void set_flashlight(int state);

#endif