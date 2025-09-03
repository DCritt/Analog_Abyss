from settings import DARKNESS_MULTIPLIER, MAX_LIGHT_DISTANCE, INVERSE_MAX_LIGHT_DISTANCE, SCREEN_CENTER, MAX_FLASHLIGHT_SCREEN_DISTANCE, INVERSE_MAX_FLASHLIGHT_SCREEN_DISTANCE, INVERSE_DARKNESS_MULTIPLIER, INVERSE_FLASHLIGHT_DISTANCE_NEGATION

class Lighting:

    def calculate_lighting_multiplier(color, distance):
        distance_multiplier = 0 if distance > MAX_LIGHT_DISTANCE else 1 - (distance * INVERSE_MAX_LIGHT_DISTANCE)

        color_new = [color[1] * (DARKNESS_MULTIPLIER * distance_multiplier)]*3

        #print(color_new, DARKNESS_MULTIPLIER, distance_multiplier)

        return color_new
    
    def calculate_lighting_multiplier_flashlight(color, distance, screen_location):
        distance_multiplier = 0 if distance > MAX_LIGHT_DISTANCE else 1 - (distance * INVERSE_MAX_LIGHT_DISTANCE)
        inverse_distance_multiplier = 1 / (distance_multiplier + 0.00001)

        center_screen_distance = (SCREEN_CENTER[0] - screen_location[0])**2 + (SCREEN_CENTER[1] - screen_location[1])**2
        flashlight_multiplier = 1 if center_screen_distance > MAX_FLASHLIGHT_SCREEN_DISTANCE else ((INVERSE_DARKNESS_MULTIPLIER * (inverse_distance_multiplier if inverse_distance_multiplier < INVERSE_FLASHLIGHT_DISTANCE_NEGATION else INVERSE_FLASHLIGHT_DISTANCE_NEGATION)) * (max(1 - (center_screen_distance * INVERSE_MAX_FLASHLIGHT_SCREEN_DISTANCE), DARKNESS_MULTIPLIER)))
        
        return [color[1] * (distance_multiplier * flashlight_multiplier * DARKNESS_MULTIPLIER)]*3