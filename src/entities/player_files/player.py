import pygame
from src.data.settings import *
import math
from ..entity import Entity
from src.entities.player_files.states.player_states import PlayerIdleState, PlayerWalkState, PlayerSprintState, PlayerDeadState

#Player Class
class Player(Entity):
    
    def __init__(self, scene, pos):
        super().__init__(scene, pos)
        self.idle_state = PlayerIdleState(self.state_machine, self)
        self.walk_state = PlayerWalkState(self.state_machine, self)
        self.sprint_state = PlayerSprintState(self.state_machine, self)
        self.dead_state = PlayerDeadState(self.state_machine, self)
        self.state_machine.init_state(self.idle_state)
        self.sprint_mult = 1.5

    def update(self):
        keys = pygame.key.get_pressed()
        self.state_machine.state.check_inputs(keys)
        self.state_machine.state.update(keys)

    def event_update(self, event):
        self.state_machine.state.check_event(event)

    def check_wall_col_x(self):
        pass

    def get_move_dir(self, keys):
        sin = math.sin(self.angle)
        cos = math.cos(self.angle)

        inp_x = (keys[pygame.K_a] - keys[pygame.K_d])
        inp_y = (keys[pygame.K_w] - keys[pygame.K_s])

        dir = pygame.Vector2((inp_x * sin) + (inp_y * cos), (inp_y * sin) - (inp_x * cos))

        if dir.length_squared() > 0:
            dir = dir.normalize()

        return dir
    
    def get_rot_dir(self, keys):
        return (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])

    def draw_2d(self):
        #pygame.draw.line(
        #   self.game.screen, 
        #    'green', 
        #    (self.x * 100, self.y * 100), 
        #    (self.x * 100 + WIDTH * math.cos(self.player_angle), self.y * 100 + WIDTH * math.sin(self.player_angle)),
        #    2
        #)
        pygame.draw.circle(self.game.screen, 'blue', (self.x * 100, self.y * 100), 20)