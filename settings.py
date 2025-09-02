import math

#screen settings
RESOLUTION = WIDTH, HEIGHT = 1200, 700
FPS = 120

#3D projection settings
FOV = math.pi / 3
RAY_AMT = WIDTH // 4
RAY_DELTA_ANGLE = FOV / RAY_AMT
MAX_DEPTH = 15
RAY_WIDTH_SCALE = WIDTH / RAY_AMT
SCREEN_DISTANCE = (WIDTH / 2) / math.tan(FOV / 2)