import pygame
import platform
import pathlib as Path
import ctypes
from src.data.settings import *
from src.audio.audio_manager import AudioManager
from src.image.image_manager import ImageManager

class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.scene = None
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.running = True

        lib_name = "mygraphics.dll" if platform.system() == "Windows" else "mygraphics.so"
        curr_dir = Path.Path(__file__).resolve().parent.parent.parent
        lib_path = curr_dir / "libs" / "graphics_lib" / lib_name
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
            ctypes.c_double,
            ctypes.c_double
        ]
        self.graphics_lib.set_darkness.argtypes = [
            ctypes.c_double,
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
        self.graphics_lib.set_flashlight.argtypes = [
            ctypes.c_int
        ]

        self.graphics_lib.init_lighting_settings(HEIGHT, DARKNESS_MULTIPLIER, MAX_LIGHT_DISTANCE)
        self.graphics_lib.init_graphics(WIDTH, HEIGHT, DEFINITION)

        texture_dir = curr_dir / "assets" / "sprites" / "wall_textures"
        file_paths = [str(texture_dir / "metal.ppm"), str(texture_dir / "electric.ppm")]
        num_paths = len(file_paths)

        c_file_paths_array = []
        for file in file_paths:
            file_path = file.encode('utf-8') + b'\0'
            buf = ctypes.create_string_buffer(file_path)
            c_file_paths_array.append(buf)

        path_type = ctypes.POINTER(ctypes.c_char) * num_paths
        c_file_paths = path_type(*[ctypes.cast(buf, ctypes.POINTER(ctypes.c_char)) for buf in c_file_paths_array])

        self.graphics_lib.init_textures(c_file_paths, num_paths, 64)

        self.audio_manager = AudioManager()
        self.audio_manager.init_sounds(curr_dir)

        self.image_manager = ImageManager()
        self.image_manager.init_images(curr_dir)

    def load_scene(self, scene):
        self.scene = scene

    def update(self):
        self.delta_time = self.clock.tick(FPS) / 1000
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        self.scene.update()
        pygame.display.update()

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quit_game()

            self.scene.check_event(event)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.scene.draw()

    def run(self):
        while self.running == True:
            self.update()
            self.check_events()
            self.draw()

    def quit_game(self):
        self.running = False
        self.graphics_lib.free_map()
        self.graphics_lib.free_textures()