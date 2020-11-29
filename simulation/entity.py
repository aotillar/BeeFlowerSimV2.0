from .state_machine import State
import random as rn


def random_number():
    return rn.randint(0, 1)


class WorldEntity:
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.state = State()
        self.name = name

    def notify(self, message):
        print(self.name + ": >>> Out >>> : " + message)
        self.mediator.notify(message, self)

    def receive(self, message):
        print(self.name + ": <<< In <<< : " + message)

    def update(self):
        self.state.action(random_number())
        self.notify(self.state.state_id)
