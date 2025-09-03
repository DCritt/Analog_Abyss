from settings import DARKNESS_MULTIPLIER, MAX_LIGHT_DISTANCE, INVERSE_MAX_LIGHT_DISTANCE, SCREEN_CENTER

class Lighting:

    def calculate_lighting_multiplier(color, distance):
        distance_multiplier = 0 if distance > MAX_LIGHT_DISTANCE else distance * INVERSE_MAX_LIGHT_DISTANCE

        return [color * (distance_multiplier * DARKNESS_MULTIPLIER)]
    
    def calculate_lighting_multiplier(color, distance, screen_location):
        