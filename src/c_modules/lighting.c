#include "lighting.h"

double MAX_FLASHLIGHT_SCREEN_DISTANCE;
double darkness_multiplier;
double max_light_distance;

double (*lighting_multiplier_func)(double, double) = calculate_lighting_multiplier_f;
int flashlight = 1;

void init_lighting_settings(int height, double dark_mult, double max_light_dist) {
    MAX_FLASHLIGHT_SCREEN_DISTANCE = (pow(((height / 2) * 0.9), 2));
    darkness_multiplier = dark_mult;
    max_light_distance = max_light_dist;
}

void set_darkness(double dark_mult, double max_light_dist) {
    darkness_multiplier = dark_mult;
    max_light_distance = max_light_dist;
}

double calculate_lighting_multiplier_f(double center_screen_dist, double dist) {
    double dist_mult = (dist > max_light_distance) ? 0 : (1 - (dist / max_light_distance));   

    double dist_negation = ((1 / dist_mult) < INVERSE_FLASHLIGHT_DISTANCE_NEGATION) ? (1 / dist_mult) : INVERSE_FLASHLIGHT_DISTANCE_NEGATION;
    
    double screen_dist_proportion = 1 - (center_screen_dist / MAX_FLASHLIGHT_SCREEN_DISTANCE);
    double dist_from_center_mult = (screen_dist_proportion < darkness_multiplier) ? darkness_multiplier : screen_dist_proportion;

    return (darkness_multiplier * dist_mult * (((1 / darkness_multiplier) * dist_negation) * dist_from_center_mult));
}

double calculate_lighting_multiplier_nf(double center_screen_dist, double dist) {
    double dist_mult = (dist > max_light_distance) ? 0 : (1 - (dist / max_light_distance));   

    return (darkness_multiplier * dist_mult);
}

void set_flashlight(int state) {
    flashlight = state;
    lighting_multiplier_func = flashlight
        ? calculate_lighting_multiplier_f
        : calculate_lighting_multiplier_nf;
}