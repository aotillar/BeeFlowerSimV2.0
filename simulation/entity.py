from .state_machine import State
import random as rn
import itertools


def random_number():
    return rn.randint(0, 1)


class WorldEntity:
    newid = itertools.count(100, 1)

    def __init__(self, name,mediator):
        self.id = next(WorldEntity.newid)
        self.name = name
        self.mediator = mediator

    def notify(self, message):
        print(self.name, ": >>> Out >>> : ", message)
        self.mediator.notify(message, self)

    def receive(self, message):
        print(self.name, ": <<< In <<< : ", message)


    @staticmethod
    def create_message(sender: object, receiver: str, message: object, extra: object = None) -> object:
        message = {
            'sender': sender,
            'receiver': receiver,
            'message': message,
            'extra': extra
        }
        return message

    def update(self):
        pass
