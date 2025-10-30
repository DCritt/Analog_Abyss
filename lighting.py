from settings import DARKNESS_MULTIPLIER, INVERSE_MAX_FLASHLIGHT_SCREEN_DISTANCE, INVERSE_DARKNESS_MULTIPLIER, INVERSE_FLASHLIGHT_DISTANCE_NEGATION

class Lighting:
    
    def calculate_flashlight_multiplier(center_screen_distance, inverse_distance_multiplier):
        distance_negation = inverse_distance_multiplier if inverse_distance_multiplier < INVERSE_FLASHLIGHT_DISTANCE_NEGATION else INVERSE_FLASHLIGHT_DISTANCE_NEGATION
        
        screen_distance_proportion = 1 - (center_screen_distance * INVERSE_MAX_FLASHLIGHT_SCREEN_DISTANCE)
        distance_from_center_multiplier = DARKNESS_MULTIPLIER if (screen_distance_proportion < DARKNESS_MULTIPLIER) else screen_distance_proportion

        return ((INVERSE_DARKNESS_MULTIPLIER * distance_negation) * distance_from_center_multiplier)