import pygame
import platform
import pathlib as Path
import ctypes
from settings import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.scene = None
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.running = True

        lib_name = "mygraphics.dll" if platform.system() == "Windows" else "mygraphics.so"
        curr_dir = Path.Path(__file__).resolve().parent
        lib_path = curr_dir / "Object_Linker_Files" / lib_name
        self.graphics_lib = ctypes.CDLL(str(lib_path))

        self.graphics_lib.generate_pixels.restype = ctypes.POINTER(ctypes.c_uint8)
        self.graphics_lib.generate_pixels.argtypes = [
            ctypes.POINTER(ctypes.c_double * 2),
            ctypes.POINTER(ctypes.c_int * 2),
            ctypes.c_double
        ]
        self.graphics_lib.free_pixels.argtypes = [
            ctypes.POINTER(ctypes.c_uint8)
        ]
        self.graphics_lib.init_graphics.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int
        ]
        self.graphics_lib.init_lighting_settings.argtypes = [
            ctypes.c_int,
            ctypes.c_double
        ]
        self.graphics_lib.set_map.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8))
        ]

        self.graphics_lib.init_textures.argtypes = [
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char)),
            ctypes.c_int,
            ctypes.c_int
        ]

        self.graphics_lib.init_lighting_settings(HEIGHT, DARKNESS_MULTIPLIER)
        self.graphics_lib.init_graphics(WIDTH, HEIGHT, DEFINITION)

        texture_dir = curr_dir / "Sprites" / "Wall_Textures"
        file_paths = [file for file in texture_dir.iterdir()]
        num_paths = len(file_paths)

        c_file_paths_array = []
        for file in file_paths:
            file_path = str(file).encode('utf-8') + b'\0'
            buf = ctypes.create_string_buffer(file_path)
            c_file_paths_array.append(buf)

        path_type = ctypes.POINTER(ctypes.c_char) * num_paths
        c_file_paths = path_type(*[ctypes.cast(buf, ctypes.POINTER(ctypes.c_char)) for buf in c_file_paths_array])

        self.graphics_lib.init_textures(c_file_paths, num_paths, 64)

    def load_scene(self, scene):
        self.scene = scene

    def update(self):
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        self.scene.update()
        pygame.display.update()

    def check_events(self):
        events = pygame.event.get()
        self.scene.check_events(events)

    def draw(self):
        self.scene.draw()

    def run(self):
        while self.running == True:
            self.update()
            self.check_events()
            self.draw()