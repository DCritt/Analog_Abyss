import pygame
from src.state_management.state import State

#Base Player State Class
class PlayerState(State):
    def __init__(self, state_machine, player):
        super().__init__(state_machine)
        self.player = player

    def update(self, keys):
        pass

    def check_states(self, keys):
        pass

    def check_event(self, event):
        pass

    def enter(self):
        pass

    def exit(self):
        pass

#Child Player State Classes

#Child Player Disabled State Class
class PlayerDisabledState(PlayerState):
    def __init__(self, state_machine, player):
        super().__init__(state_machine, player)

#Child Player Enabled State Class
class PlayerEnabledState(PlayerState):
    def __init__(self, state_machine, player):
        super().__init__(state_machine, player)

    def check_event(self, event):
        if event.key == pygame.K_f:
            self.player.toggle_flashlight()

#Child Player Idle State Class
class PlayerIdleState(PlayerEnabledState):
    def __init__(self, state_machine, player):
        super().__init__(state_machine, player)

    def update(self, keys):
        rot_dir = self.player.get_rot_dir(keys)
        self.player.rotate(rot_dir)

    def check_states(self, keys):
        is_moving = (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d])
        is_sprinting = (keys[pygame.K_LSHIFT] and is_moving and self.player.stamina > 0)
        
        if (is_sprinting):
            self.state_machine.change_state(self.player.sprint_state)
        elif (is_moving):
            self.state_machine.change_state(self.player.walk_state)

    def check_event(self, event):
        super().check_event(event)

    def enter(self):
        pass

    def exit(self):
        pass

#Child Player Walk State Class
class PlayerWalkState(PlayerEnabledState):
    def __init__(self, state_machine, player):
        super().__init__(state_machine, player)

    def update(self, keys):
        move_dir = self.player.get_move_dir(keys)
        rot_dir = self.player.get_rot_dir(keys)
        self.player.move(move_dir)
        self.player.rotate(rot_dir)

    def check_states(self, keys):
        is_moving = (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d])
        is_sprinting = (keys[pygame.K_LSHIFT] and self.player.stamina > 0)

        if (not is_moving):
            self.state_machine.change_state(self.player.idle_state)
        elif (is_sprinting):
            self.state_machine.change_state(self.player.sprint_state)

    def check_event(self, event):
        super().check_event(event)

    def enter(self):
        pass

    def exit(self):
        pass

#Child Player Sprint State Class
class PlayerSprintState(PlayerEnabledState):
    def __init__(self, state_machine, player):
        super().__init__(state_machine, player)
        self.speed_mult = 1.5

    def update(self, keys):
        move_dir = self.player.get_move_dir(keys)
        rot_dir = self.player.get_rot_dir(keys)
        self.player.move(move_dir)
        self.player.rotate(rot_dir)

    def check_states(self, keys):
        is_moving = (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d])
        is_sprinting = (keys[pygame.K_LSHIFT] and self.player.stamina > 0)

        if (not is_moving):
            self.state_machine.change_state(self.player.idle_state)
        elif(not is_sprinting):
            self.state_machine.change_state(self.player.walk_state)

    def check_event(self, event):
        super().check_event(event)

    def enter(self):
        pass

    def exit(self):
        pass

#Child Player Dead State Class
class PlayerDeadState(PlayerDisabledState):
    def __init__(self, state_machine, player):
        super().__init__(state_machine, player)

    def update(self, keys):
        pass

    def check_states(self, keys):
        pass

    def check_event(self, event):
        pass

    def enter(self):
        pass

    def exit(self):
        pass