#include "lighting.h"

double calculate_lighting_multiplier(double dark_mult, double center_screen_dist, double dist, double max_dist) {
    double dist_mult = (dist > max_dist) ? 0 : (1 - (dist / max_dist));   

    double dist_negation = ((1 / dist_mult) < INVERSE_FLASHLIGHT_DISTANCE_NEGATION) ? (1 / dist_mult) : INVERSE_FLASHLIGHT_DISTANCE_NEGATION;
    
    double screen_dist_proportion = 1 - (center_screen_dist / MAX_FLASHLIGHT_SCREEN_DISTANCE);
    double dist_from_center_mult = (screen_dist_proportion < dark_mult) ? dark_mult : screen_dist_proportion;

    return (dark_mult * dist_mult * (((1 / dark_mult) * dist_negation) * dist_from_center_mult));
}