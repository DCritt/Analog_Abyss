import math

#screen settings
RESOLUTION = WIDTH, HEIGHT = 1200, 700
FPS = 60

#raycasting settings
FOV = math.pi / 3
RAY_AMT = WIDTH // 2
RAY_DELTA_ANGLE = FOV / RAY_AMT
MAX_DEPTH = 20

#3D projection settings
SCREEN_DISTANCE = (WIDTH / 2) / math.tan(FOV / 2)
RAY_WIDTH_SCALE = WIDTH / RAY_AMT