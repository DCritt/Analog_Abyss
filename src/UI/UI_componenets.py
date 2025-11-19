import pygame
from src.data.settings import *

class UIComponent:
    def __init__(self, x_p, y_p, width_p, height_p):
        self.x_p = x_p
        self.y_p = y_p
        self.width_p = width_p
        self.height_p = height_p
        self.rect = pygame.Rect(x_p * WIDTH, y_p * HEIGHT, width_p * WIDTH, height_p * HEIGHT)
        self.parent = None
        self.visible = True
        self.active = True

    def update(self):
        pass

    def check_event(self, event):
        pass

    def draw(self, surface):
        pass

    def set_parent(self, parent):
        self.parent = parent
        x = (self.x_p * parent.rect.x)
        y = (self.y_p * parent.rect.y)
        width = (self.width_p * parent.rect.width)
        height = (self.height_p * parent.rect.height)
        self.rect = pygame.Rect(x, y, width, height)

    def resize(self, x_p, y_p, width_p, height_p):
        parent_dim = (WIDTH, HEIGHT) if not self.parent else (self.parent.rect.width, self.parent.rect.height)

        self.x_p = x_p
        self.y_p = y_p
        self.width_p = width_p
        self.height_p = height_p
        self.rect = pygame.Rect((x_p * parent_dim[0]), (y_p * parent_dim[1]), (width_p * WIDTH), (height_p * HEIGHT))

    def get_relative_rect(self):
        parent_rect = self.parent.get_relative_rect() if self.parent else (0, 0, 0, 0)
        return pygame.Rect((self.rect.x + parent_rect[0]), (self.rect.y + parent_rect[1]), self.rect.width, self.rect.height)

class UIPanel(UIComponent):
    def __init__(self, x_p, y_p, width_p, height_p, children=[]):
        super().__init__(x_p, y_p, width_p, height_p)
        
        self.children = children
        for child in children:
            child.set_parent(self)

        self.surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)

    def update(self):
        for child in self.children:
            child.update()

    def check_event(self, event):
        for child in self.children:
            child.check_event(event)

    def draw(self, surface):
        for child in self.children:
            child.draw(self.surface)
        surface.blit(self.surface, (self.rect.x, self.rect.y))

    def set_parent(self, parent):
        super().set_parent(parent)
        self.surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
    
    def resize(self, x_p, y_p, width_p, height_p):
        super().resize(x_p, y_p, width_p, height_p)
        self.surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        for child in self.children:
            child.resize(child.x_p, child.y_p, child.width_p, child.height_p)

    def add_child(self, child):
        self.children.append(child)

class UILabel(UIComponent):
    def __init__(self, x_p, y_p, text, font_size, color):
        self.text = text
        self.font = pygame.font.Font(None, ((int)(font_size * SCALE_SIZE)))
        self.color = color
        self.surface = self.font.render(text, True, color)

        width_p = self.surface.get_width() / WIDTH
        height_p = self.surface.get_height() / HEIGHT
        super().__init__(x_p, y_p, width_p, height_p)

    def update(self):
        pass

    def check_event(self, event):
        pass

    def draw(self, surface):
        surface.blit(self.surface, (self.rect.x, self.rect.y))

    def resize(self, x_p, y_p, width_p, height_p):
        parent_dim = (WIDTH, HEIGHT) if not self.parent else (self.parent.rect.width, self.parent.rect.height)
        
        self.surface = self.font = pygame.font.Font(None, ((int)(font_size * SCALE_SIZE)))
        width_p = self.surface.get_width() / parent_dim[0]
        height_p = self.surface.get_height() / parent_dim[1]

        self.resize(x_p, y_p, width_p, height_p)

class UIButton(UIComponent):
    def __init__(self, x_p, y_p, width_p, height_p, text, font_size, font_color, color, func):
        super().__init__(x_p, y_p, width_p, height_p)

        self.text = text
        self.font = pygame.font.Font(None, ((int)(font_size * SCALE_SIZE)))
        self.font_color = font_color
        self.font_surface = self.font.render(text, True, font_color)
        
        self.color = color
        self.hover_color = ((color[0] // 2), (color[1] // 2), (color[2] // 2))

        self.func = func
        self.hovered = False

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.get_relative_rect().collidepoint(mouse_pos)
        
    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.hovered:
                self.func()

    def draw(self, surface):
        pygame.draw.rect(surface, (self.color if not self.hovered else self.hover_color), self.rect)
        surface.blit(self.font_surface, (self.rect.x, self.rect.y))

class UIImage(UIComponent):
    def __init__(self, x_p, y_p, width_p, height_p, image_path):
        super().__init__(x_p, y_p, width_p, height_p)

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, ((int)(width_p * WIDTH), (int)(height_p * HEIGHT)))

    def update(self):
        pass

    def check_event(self, event):
        pass

    def draw(self, surface):
        pass