import time
import random as rn
import itertools


class Mediator():
    def __init__(self):
        self.components = []

    def add(self, component):
        self.components.append(component)

    def notify(self, message, component):
        for _component in self.components:
            if _component != component:
                _component.receive(message)


class State:
    def __init__(self, starting_state):
        self.new_state(starting_state)

    def new_state(self, state):
        self.__class__ = state

    def action(self, x):
        raise NotImplementedError()


class State_A(State):
    state_id = 'a'

    def action(self, x):
        time.sleep(.1)
        if x == 1:
            self.new_state(State_B)
        else:
            self.new_state(State_A)


class State_B(State):
    state_id = 'b'

    def action(self, x):
        time.sleep(.1)
        if x == 1:
            self.new_state(State_C)
        else:
            self.new_state(State_B)


class State_C(State):
    state_id = 'c'

    def action(self, x):
        time.sleep(.1)
        if x == 1:
            self.new_state(State_A)
        else:
            self.new_state(State_C)


class Component:
    newid = itertools.count()

    def __init__(self, mediator, name, starting_state):
        self.id = next(Component.newid)
        self.mediator = mediator
        self.name = name
        self.state = State(starting_state)

    def notify(self, message):
        print(self.name, ": >>> Out >>> : ", message)
        self.mediator.notify(message, self)

    def receive(self, message):
        print(self.name, ": <<< In <<< : ", message)

    def random_number(self):
        return rn.randint(0, 1)

    def update(self):
        self.state.action(self.random_number())
        self.notify(self.state.state_id)


class World:
    newid = itertools.count()

    def __init__(self, mediator, name):
        self.id = next(Component.newid)
        self.mediator = mediator
        self.name = name
        self.time = 0

    def notify(self, message):
        print(self.name, ": >>> Out >>> : ", message)
        self.mediator.notify(message, self)

    def receive(self, message):
        print(self.name, ": <<< In <<< : ", message)

    def update(self):
        if self.time < 24:
            self.time += 1
            self.notify(self.time)
        elif self.time == 24:
            self.time = 0
            self.notify(self.time)


def main():
    mdr = Mediator()
    c1 = Component(mdr, 'C1', State_A)
    c2 = Component(mdr, 'C2', State_B)
    c3 = Component(mdr, 'C3', State_C)
    w = World(mdr, 'w')

    mdr.add(c1)
    mdr.add(c2)
    mdr.add(c3)
    mdr.add(w)

    x = 0
    while x == 0:
        w.update()
        c1.update()
        print(' ')
        c2.update()
        print(' ')
        c3.update()
        print(' ')



if __name__ == '__main__':
    main()



