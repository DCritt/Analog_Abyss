#include "lighting.h"

double MAX_FLASHLIGHT_SCREEN_DISTANCE;
double DARKNESS_MULTIPLIER;

double (*lighting_multiplier_func)(double, double, double) = calculate_lighting_multiplier_f;
int flashlight = 1;

void init_lighting_settings(int height, double dark_mult) {
    MAX_FLASHLIGHT_SCREEN_DISTANCE = (pow(((height / 2) * 0.9), 2));
    DARKNESS_MULTIPLIER = dark_mult;
}

double calculate_lighting_multiplier_f(double center_screen_dist, double dist, double max_dist) {
    double dist_mult = (dist > max_dist) ? 0 : (1 - (dist / max_dist));   

    double dist_negation = ((1 / dist_mult) < INVERSE_FLASHLIGHT_DISTANCE_NEGATION) ? (1 / dist_mult) : INVERSE_FLASHLIGHT_DISTANCE_NEGATION;
    
    double screen_dist_proportion = 1 - (center_screen_dist / MAX_FLASHLIGHT_SCREEN_DISTANCE);
    double dist_from_center_mult = (screen_dist_proportion < DARKNESS_MULTIPLIER) ? DARKNESS_MULTIPLIER : screen_dist_proportion;

    return (DARKNESS_MULTIPLIER * dist_mult * (((1 / DARKNESS_MULTIPLIER) * dist_negation) * dist_from_center_mult));
}

double calculate_lighting_multiplier_nf(double center_screen_dist, double dist, double max_dist) {
    double dist_mult = (dist > max_dist) ? 0 : (1 - (dist / max_dist));   

    return (DARKNESS_MULTIPLIER * dist_mult);
}

void toggle_flashlight() {
    flashlight = !flashlight;
    lighting_multiplier_func = flashlight
        ? calculate_lighting_multiplier_f
        : calculate_lighting_multiplier_nf;
}