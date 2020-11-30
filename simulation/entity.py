import random as rn
import itertools
import time


def random_number():
    return rn.randint(0, 1)


class WorldEntity:
    newid = itertools.count(1000)

    def __init__(self, name, mediator):
        self.id = next(WorldEntity.newid)
        self.name = name
        self.mediator = mediator


    @staticmethod
    def create_message(sender: object, receiver: str, message: object, extra: object = None) -> object:
        message = {
            'sender': sender,
            'receiver': receiver,
            'message': message,
            'time':time.perf_counter(),
            'extra': extra
        }
        return message
