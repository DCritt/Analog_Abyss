import pygame
from src.data.settings import *
import math
from src.entities.entity import Entity
from src.entities.player_files.states.player_states import PlayerIdleState, PlayerWalkState, PlayerSprintState, PlayerDeadState
from src.UI.UI_screens.player_interface import PlayerInterface

#Player Class
class Player(Entity):
    
    def __init__(self, scene, pos):
        super().__init__(scene, pos, size=0.4, speed=4, rot_speed=3)

        self.lib = self.game.graphics_lib
        
        self.idle_state = PlayerIdleState(self.state_machine, self)
        self.walk_state = PlayerWalkState(self.state_machine, self)
        self.sprint_state = PlayerSprintState(self.state_machine, self)
        self.dead_state = PlayerDeadState(self.state_machine, self)
        self.state_machine.init_state(self.idle_state)
        
        self.sprint_mult = 1.5
        self.max_stamina = 100.0
        self.stamina = self.max_stamina
        self.stamina_drain = 5.0
        self.stamina_regen = 10.0
        self.stamina_delay = 4.0
        self.stamina_timer = 4.0

        self.max_sanity = 100.0
        self.sanity = self.max_stamina
        self.flashlight_sanity_drain = 0.25

        self.max_battery = 100.0
        self.battery = self.max_battery
        self.flashlight_on = True
        self.flashlight_drain = 0.25
        
        self.footstep_effects = ["low_step", "med_step", "high_step"]

        self.player_ui = PlayerInterface(self.game, self)
        

    def update(self):
        keys = pygame.key.get_pressed()
        self.update_stamina()
        self.update_battery()
        self.update_sanity()
        self.state_machine.state.check_states(keys)
        self.state_machine.state.update(keys)
        self.player_ui.update()
        

    def event_update(self, event):
        self.state_machine.state.check_event(event)
        self.player_ui.check_event(event)

    def get_move_dir(self, keys):
        sin = math.sin(self.angle)
        cos = math.cos(self.angle)

        inp_x = (keys[pygame.K_a] - keys[pygame.K_d])
        inp_y = (keys[pygame.K_w] - keys[pygame.K_s])

        dir = pygame.Vector2((inp_x * sin) + (inp_y * cos), (inp_y * sin) - (inp_x * cos))

        dir = dir.normalize()

        return dir
    
    def get_rot_dir(self, keys):
        return (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])

    def update_stamina(self):
        if self.state_machine.state == self.sprint_state:
            self.stamina -= (self.stamina_drain * self.game.delta_time)
            self.stamina = self.stamina if self.stamina >= 0 else 0
            self.stamina_timer = 0
        else:
            if self.stamina_timer < self.stamina_delay:
                self.stamina_timer += self.game.delta_time
            else:
                self.stamina += (self.stamina_regen * self.game.delta_time)
                self.stamina = self.stamina if self.stamina <= self.max_stamina else self.max_stamina

    def update_sanity(self):
        if not self.flashlight_on:
            self.sanity -= (self.flashlight_sanity_drain * self.game.delta_time)
            self.sanity = self.sanity if self.sanity >= 0 else 0

        sanity_prop = self.sanity / self.max_sanity

        darkness_mult = MIN_DARKNESS_MULTIPLIER + (DARKNESS_MULTIPLIER_RANGE * sanity_prop)
        light_distance = MIN_LIGHT_DISTANCE + (LIGHT_DISTANCE_RANGE * sanity_prop)

        self.lib.set_darkness(darkness_mult, light_distance)

    def update_battery(self):
        if self.flashlight_on:
            self.battery -= (self.flashlight_drain * self.game.delta_time)
            if self.battery <= 0:
                self.battery = 0
                self.toggle_flashlight()

    def toggle_flashlight(self):
        if self.battery > 0:
            self.flashlight_on = not self.flashlight_on
            self.lib.set_flashlight(self.flashlight_on)
        else:
            self.flashlight_on = False
            self.lib.set_flashlight(False)

    def draw_ui(self, surface):
        self.player_ui.draw(surface)
        pass

    def draw_2d(self):
        pygame.draw.circle(self.game.screen, 'blue', (self.x * 100, self.y * 100), 20)