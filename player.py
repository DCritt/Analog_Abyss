import pygame
from settings import *
import math

class Player:
    
    def __init__(self, game):
        self.game = game
        self.x, self.y = 1.5 , 1.5
        self.player_angle = 0
        self.player_size = 60
        self.player_speed = .005
        self.player_rotation_speed = 0.004

    def move_player(self):
        speed = self.player_speed * self.game.delta_time
        speed_x = speed * math.cos(self.player_angle)
        speed_y = speed * math.sin(self.player_angle)
        dx, dy = 0, 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_x
            dy += speed_y
        if keys[pygame.K_s]:
            dx -= speed_x
            dy -= speed_y
        if keys[pygame.K_a]:
            dx += speed_y
            dy -= speed_x
        if keys[pygame.K_d]:
            dx -= speed_y
            dy += speed_x

        self.check_wall_collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.player_angle -= self.player_rotation_speed * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.player_angle += self.player_rotation_speed * self.game.delta_time

        self.player_angle %= math.tau

    def update(self):
        self.move_player()

    def check_wall_collision(self, dx, dy):
        player_size_scale = self.player_size / self.game.delta_time
        if (int(self.x + dx * player_size_scale), int(self.y)) not in self.game.map.map_dic:
            self.x += dx
        if (int(self.x), int(self.y + dy * player_size_scale)) not in self.game.map.map_dic:
            self.y += dy

    def draw(self):
        #pygame.draw.line(
        #   self.game.screen, 
        #    'green', 
        #    (self.x * 100, self.y * 100), 
        #    (self.x * 100 + WIDTH * math.cos(self.player_angle), self.y * 100 + WIDTH * math.sin(self.player_angle)),
        #    2
        #)
        pygame.draw.circle(self.game.screen, 'blue', (self.x * 100, self.y * 100), 20)

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)