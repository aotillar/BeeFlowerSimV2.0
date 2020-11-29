from .state_machine import State
import random as rn
import itertools


def random_number():
    return rn.randint(0, 1)


class WorldEntity:
    newid = itertools.count(100, 1)

    def __init__(self, mediator, name):
        self.name = name
        self.id = next(WorldEntity.newid)
        self.mediator = mediator
        self.state = State()

    @staticmethod
    def create_message(sender: object, receiver: str, message: object, extra: object = None) -> object:
        message = {
            'sender': sender,
            'receiver': receiver,
            'message': message,
            'extra': extra
        }
        return message

    def notify(self, message):
        print(self.name , ": >>> Out >>> : " , message)
        self.mediator.notify(message, self)

    def receive(self, message):
        print(self.name ,": <<< In <<< : " ,message)

    def update(self):
        self.state.action(random_number())
        self.notify(self.create_message(self.id, 'entities', self.state.state_id, ))
