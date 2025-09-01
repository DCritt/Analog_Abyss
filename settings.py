import math

#screen settings
RESOLUTION = WIDTH, HEIGHT = 2500, 1400
FPS = 10

#raycasting settings
FOV = math.pi / 3
RAY_AMT = WIDTH // 2
RAY_DELTA_ANGLE = FOV / RAY_AMT
MAX_DEPTH = 20