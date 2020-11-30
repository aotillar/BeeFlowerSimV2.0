import time


class State:
    def __init__(self):
        self.new_state(StateA)

    def new_state(self, state):
        self.__class__ = state

    def action(self, x):
        raise NotImplementedError()


class StateA(State):
    state_id = 'a'

    def action(self, x):
        # print('Inside State A')
        # time.sleep(.1)
        if x == 1:
            self.new_state(StateB)
        else:
            self.new_state(StateA)


class StateB(State):
    state_id = 'b'

    def action(self, x):
        # print('Inside State B')
        # time.sleep(.1)
        if x == 1:
            self.new_state(StateC)
        else:
            self.new_state(StateB)


class StateC(State):
    state_id = 'c'

    def action(self, x):
        # print('Inside State C')
        # time.sleep(.1)
        if x == 1:
            self.new_state(StateA)
        else:
            self.new_state(StateC)
