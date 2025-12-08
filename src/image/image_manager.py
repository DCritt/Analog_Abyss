import pygame

class ImageManager:
    def __init__(self):
        self.images = {}

    def init_images(self, root_dir):
        sprite_path = root_dir / "assets" / "sprites"

        UI_path = sprite_path / "UI"
        player_UI_path = UI_path / "player_UI"

        flashlight_path = player_UI_path / "flashlight.png"
        self.load_image("flashlight", str(flashlight_path))

    def load_image(self, name, path):
        self.images[name] = pygame.image.load(path).convert_alpha()

    def get_image(self, name):
        if name not in self.images:
            return None
        return self.images[name]