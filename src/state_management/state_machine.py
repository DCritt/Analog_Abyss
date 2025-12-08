import pygame

#Base State Machine Class
class StateMachine:
    def __init__(self):
        self.state = None

    def init_state(self, state):
        self.state = state
        self.state.enter()

    def change_state(self, state):
        self.state.exit()
        self.state = state
        self.state.enter()