import pygame

#Base State Class
class State:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.speed_mult = 1.0

    def update(self):
        pass

    def check_inputs(self):
        pass

    def check_event(self, event):
        pass

    def enter(self):
        pass

    def exit(self):
        pass