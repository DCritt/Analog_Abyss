import math

#screen settings
RESOLUTION = WIDTH, HEIGHT = 2500, 1400
FPS = 60

#3D projection settings
FOV = math.pi / 3
RAY_AMT = WIDTH // 16
LIGHT_SEG_SIZE = 16
RAY_DELTA_ANGLE = FOV / RAY_AMT
MAX_DEPTH = 15
RAY_WIDTH_SCALE = WIDTH // RAY_AMT
SCREEN_DISTANCE = (WIDTH / 2) / math.tan(FOV / 2)