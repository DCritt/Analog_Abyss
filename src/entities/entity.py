import pygame
from src.state_management.state_machine import StateMachine

class Entity:
    def __init__(self, scene, pos):
        self.scene = scene
        self.game = scene.game
        self.map = scene.map
        self.lib = self.game.graphics_lib
        self.state_machine = StateMachine()
        self.x, self.y = pos
        self.vel_x, self.vel_y = (0.0, 0.0)
        self.angle = 0
        self.size = 60
        self.speed = 0.005
        self.rotation_speed = 0.002

    def move(self, move_dir):
        speed = self.speed * self.state_machine.state.speed_mult * self.game.delta_time
        self.vel_x = speed * move_dir.x
        self.vel_y = speed * move_dir.y

        self.x += self.vel_x
        self.y += self.vel_y
    
    def rotate(self, rot_dir):
        rot_speed = self.rotation_speed * rot_dir * self.game.delta_time
        self.angle += rot_speed

    def update(self):
        pass

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
