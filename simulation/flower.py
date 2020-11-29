from .entity import WorldEntity
from .state_machine import State
import itertools


class Flower(WorldEntity):
    newid = itertools.count(3000)

    def __init__(self, mediator, name):
        super().__init__(mediator, name)
        self.id = next(Flower.newid)
        self.name = name
        self.state = State()
        self.mediator = mediator

    def notify(self, message):
        print(self.name, ": >>> Out >>> : ", message)
        self.mediator.notify(message, self)

    def receive(self, message):
        print(self.name, ": <<< In <<< : ", message)


    def update(self):
        self.state.action(1)
        self.notify(self.create_message(self.id, 'bee', self.state.state_id, ))
