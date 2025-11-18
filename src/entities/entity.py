import pygame
from src.state_management.state_machine import StateMachine

class Entity:
    def __init__(self, scene, pos, size, speed, rot_speed):
        self.scene = scene
        self.game = scene.game
        self.map = scene.map
        self.state_machine = StateMachine()
        self.x, self.y = pos
        self.vel_x, self.vel_y = (0.0, 0.0)
        self.angle = 0
        self.col_radius = size / 2
        self.speed = speed
        self.rot_speed = rot_speed

    def move(self, move_dir):
        speed = self.speed * self.state_machine.state.speed_mult * self.game.delta_time
        self.vel_x = speed * move_dir.x
        self.vel_y = speed * move_dir.y

        if not self.check_collision(self.vel_x, 0):
            self.x += self.vel_x
        
        if not self.check_collision(0, self.vel_y):
            self.y += self.vel_y
    
    def rotate(self, rot_dir):
        rot_speed = self.rot_speed * rot_dir * self.game.delta_time
        self.angle += rot_speed

    def check_collision(self, dx, dy):
        left = int(self.x - self.col_radius + dx)
        right = int(self.x + self.col_radius + dx)
        top = int(self.y + self.col_radius + dy)
        bottom = int(self.y - self.col_radius + dy)

        for x in range(left, (right + 1)):
            for y in range(bottom, (top + 1)):
                if (self.map.map_arr[y][x] != 0):
                    return True
            
        return False

    def update(self):
        pass

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
