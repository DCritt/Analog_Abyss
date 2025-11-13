import pygame

#Base State Machine Class
class StateMachine:
    def __init__(self, state):
        self.state = state
        state.enter()

    def change_state(self, state):
        self.state.exit()
        self.state = state
        self.state.enter()

#Base State Class
class State:
    def __init__(self, state_machine):
        self.state_machine = state_machine

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

#Base Player State Class
class PlayerState(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)

    def update(self):
        super().update()

    def check_inputs(self):
        super().check_inputs()

    def check_event(self, event):
        super().check_event(event)

    def enter(self):
        super().enter()

    def exit(self):
        super().exit()


#Child Player State Class
class PlayerIdleState(PlayerState):
    def __init__(self, state_machine):
        super().__init__(state_machine)

    def update(self):
        super().update()

    def check_inputs(self):
        super().check_inputs()

    def check_event(self, event):
        super().check_event(event)

    def enter(self):
        super().enter()

    def exit(self):
        super().exit()