import pygame

class UIComponent:
    def __init__(self, x, y, width, height, parent):
        self.rect = pygame.Rect(x, y, width, height)
        self.parent = parent
        self.visible = True
        self.active = True

    def update(self):
        pass

    def check_event(self, event):
        pass

    def draw(self, surface):
        pass

    def get_relative_rect(self):
        parent_rect = self.parent.get_relative_rect() if self.parent else (0, 0, 0, 0)
        return pygame.rect.Rect((self.rect.x + parent_rect[0]), (self.rect.y + parent_rect[1]), self.rect.width, self.rect.height)

class UIPanel(UIComponent):
    def __init__(self, x, y, width, height, parent):
        super().__init__(x, y, width, height, parent)
        self.children = []
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

    def update(self):
        for child in self.children:
            child.update()

    def check_event(self, event):
        for child in self.children:
            child.check_event(event)

    def add_child(self, child):
        self.children.append(child)

    def draw(self, surface):
        for child in self.children:
            child.draw(self.surface)
        surface.blit(self.surface, (self.rect.x, self.rect.y))

class UILabel(UIComponent):
    def __init__(self, x, y, parent, text, font, color):
        self.text = text
        self.font = font
        self.color = color
        self.surface = font.render(text, True, color)

        width = self.surface.get_width()
        height = self.surface.get_height()
        super().__init__(x, y, width, height, parent)

    def update(self):
        pass

    def check_event(self, event):
        pass

    def draw(self, surface):
        surface.blit(self.surface, (self.rect.x, self.rect.y))

class UIButton(UIComponent):
    def __init__(self, x, y, width, height, parent, text, font, font_color, color, func):
        super().__init__(x, y, width, height, parent)

        self.text = text
        self.font = font
        self.font_color = font_color
        self.font_surface = font.render(text, True, font_color)
        
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
    def __init__(self, x, y, width, height, parent, image_path):
        super().__init__(x, y, width, height, parent)

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))

    def update(self):
        pass

    def check_event(self, event):
        pass

    def draw(self, surface):
        pass