import pygame
from src.data.settings import *

class UIComponent:
    def __init__(self, x_p, y_p, width_p, height_p):
        self.parent = None
        self.visible = True
        self.active = True
        
        self.x_p = x_p
        self.y_p = y_p
        self.width_p = width_p
        self.height_p = height_p
        self.center_rect()

    def update(self):
        pass

    def check_event(self, event):
        pass

    def draw(self, surface):
        pass

    def center_rect(self):
        parent_dim = self.get_parent_dim()

        width = (self.width_p * parent_dim[0])
        height = (self.height_p * parent_dim[1])

        x = ((self.x_p * parent_dim[0]) - (width // 2))
        x = x if x >= 0 else 0
        x = x if x <= (parent_dim[0] - width) else (parent_dim[0] - width)

        y = ((self.y_p * parent_dim[1]) - (height // 2))
        y = y if y >= 0 else 0
        y = y if y <= (parent_dim[1] - height) else (parent_dim[1] - height)

        self.rect = pygame.Rect(x, y, width, height)

    def update_rect(self):
        self.center_rect()

    def set_parent(self, parent):
        self.parent = parent
        self.update_rect()

    def resize(self, x_p, y_p, width_p, height_p):
        self.x_p = x_p
        self.y_p = y_p
        self.width_p = width_p
        self.height_p = height_p
        self.update_rect()

    def get_relative_rect(self):
        parent_rect = self.parent.get_relative_rect() if self.parent else pygame.Rect(0, 0, 0, 0)
        return pygame.Rect((self.rect.x + parent_rect[0]), (self.rect.y + parent_rect[1]), self.rect.width, self.rect.height)

    def get_valid_font(self, parent_dim):
        font_size = self.font_size

        while font_size != 0:
            font = pygame.font.Font(None, (int)(font_size * SCALE_SIZE))
            width, height = font.size(self.text)
            if (width <= parent_dim[0] and height <= parent_dim[1]):
                return font
            font_size -= 1

    def get_parent_dim(self):
        return (WIDTH, HEIGHT) if not self.parent else (self.parent.rect.width, self.parent.rect.height)

class UIPanel(UIComponent):
    def __init__(self, x_p, y_p, width_p, height_p, children=None):
        super().__init__(x_p, y_p, width_p, height_p)
        
        self.children = children if children is not None else []
        for child in self.children:
            child.set_parent(self)

        self.surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)

    def update(self):
        for child in self.children:
            child.update()

    def check_event(self, event):
        for child in self.children:
            child.check_event(event)

    def draw(self, surface):
        self.surface.fill((0, 0, 0, 0))
        for child in self.children:
            child.draw(self.surface)
        surface.blit(self.surface, (self.rect.x, self.rect.y))

    def update_rect(self):
        super().update_rect()
        self.surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        for child in self.children:
            child.update_rect()

    def set_parent(self, parent):
        super().set_parent(parent)
        for child in self.children:
            child.update_rect()
    
    def resize(self, x_p, y_p, width_p, height_p):
        super().resize(x_p, y_p, width_p, height_p)
        for child in self.children:
            child.update_rect()

    def add_child(self, child):
        self.children.append(child)
        child.set_parent(self)

class UILabel(UIComponent):
    def __init__(self, x_p, y_p, text, font_size, color):
        self.parent = None

        self.text = text
        self.font_size = font_size
        self.font = self.get_valid_font(self.get_parent_dim())
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

    def update_rect(self):
        self.font = self.get_valid_font(self.get_parent_dim())
        self.surface = self.font.render(self.text, True, self.color)


class UIButton(UIComponent):
    def __init__(self, x_p, y_p, width_p, height_p, text, font_size, font_color, color, func):
        super().__init__(x_p, y_p, width_p, height_p)

        self.text = text
        self.font_size = font_size
        self.font = self.get_valid_font((self.rect.width, self.rect.height))
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
        width_off = (self.rect.width - self.font_surface.get_width()) // 2
        height_off = (self.rect.height - self.font_surface.get_height()) // 2
        surface.blit(self.font_surface, (self.rect.x + width_off, self.rect.y + height_off))

    def update_rect(self):
        super().update_rect()
        self.font = self.get_valid_font((self.rect.width, self.rect.height))
        self.font_surface = self.font.render(self.text, True, self.font_color)

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