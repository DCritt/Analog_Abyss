import pygame
import ctypes
import platform
from pathlib import Path
from settings import RESOLUTION, WIDTH, HEIGHT, FPS, DEFINITION
from map_arrays import *
from map import *
from player import Player
from player_camera import PlayerCamera

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.running = True

        lib_name = "mygraphics.dll" if platform.system() == "Windows" else "mygraphics.so"
        curr_dir = Path(__file__).resolve().parent
        lib_path = curr_dir / "C_Files" / lib_name
        self.graphics_lib = ctypes.CDLL(str(lib_path))
        
        self.graphics_lib.generate_pixels.restype = ctypes.POINTER(ctypes.c_uint8)
        self.graphics_lib.generate_pixels.argtypes = [
            ctypes.POINTER(ctypes.c_double * 2),
            ctypes.POINTER(ctypes.c_int * 2),
            ctypes.c_double
        ]

        self.graphics_lib.init_graphics_settings.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int
        ]

        self.graphics_lib.init_lighting_settings.argtypes = [
            ctypes.c_int
        ]

        self.graphics_lib.init_graphics_settings(WIDTH, HEIGHT, DEFINITION)
        self.graphics_lib.init_lighting_settings(HEIGHT)

        self.map = Map(self, map1)
        self.player = Player(self)
        self.player_camera = PlayerCamera(self, self.player)

    def update(self):
        self.player.update()
        pygame.display.update()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')


    def draw(self):
        self.screen.fill((0, 0, 0))
        #self.map.draw()
        #self.player.draw()
        #pygame.draw.rect(self.screen, (125, 125, 125), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
        self.player_camera.draw_view()
        

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.player.event_update(event)

    def run(self):
        while self.running:
            self.check_events()
            self.draw()
            self.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()