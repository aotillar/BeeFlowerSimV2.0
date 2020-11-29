from .entity import WorldEntity
from .state_machine import State
import itertools


class Bee(WorldEntity):
    newid = itertools.count(2000)

    def __init__(self, mediator, name):
        super().__init__(mediator, name)
        self.id = next(Bee.newid)
        self.name = name
        self.state = State()
        self.mediator = mediator

    def update(self):
        self.state.action(1)
        self.notify(self.create_message(self.id, 'bee', self.state.state_id, ))
