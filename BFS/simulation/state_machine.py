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
        # print('Inside State A: BEFORE CHANGE',x)
        # time.sleep(.1)
        if x >= 32:
            self.new_state(StateB)
            # print('    STATE CHANGED')
        else:
            self.new_state(StateA)


class StateB(State):
    state_id = 'b'

    def action(self, x):
        # print('Inside State B: BEFORE CHANGE',x)
        # time.sleep(.1)
        if x >= 62:
            self.new_state(StateC)
            # print('    STATE CHANGED')
        elif x <= 32:
            self.new_state(StateA)
            # print('    STATE CHANGED')
        else:
            self.new_state(StateB)


class StateC(State):
    state_id = 'c'

    def action(self, x):
        # print('Inside State C: BEFORE CHANGE',x)
        # time.sleep(.1)
        if x <= 32:
            self.new_state(StateA)
            # print('    STATE CHANGED')
        elif x >= 62:
            self.new_state(StateB)
            # print('    STATE CHANGED')
        else:
            self.new_state(StateC)
