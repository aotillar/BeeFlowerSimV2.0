from BFS.simulation.entity import WorldEntity
from BFS.simulation.state_machine import State
import itertools
import random as rn


def random_choice(low, high):
    return rn.randint(low, high)


class Flower(WorldEntity):
    newid = itertools.count(2000)

    def __init__(self, mediator, name):
        super().__init__(mediator, name)
        self.id = next(Flower.newid)
        self.name = name
        self.state = State()
        self.mediator = mediator
        self.messages = dict()
        self.current_flower_message = None
        self.current_bee_message = None
        self.current_environment_message = {}
        self.current_environment_temperature = None
        self.current_incoming_message_id = 0

    def notify(self, message):
        # print(self.name, ": >>> Out >>> : ", message)
        self.mediator.notify(message, self)

    def receive(self, message):
        # print(self.name, ": <<< In <<< : ", message)
        self.messages[self.current_incoming_message_id] = message
        self.current_incoming_message_id += 1

    def clear_messages(self):
        self.messages.clear()
        self.current_flower_message.clear()
        self.current_bee_message.clear()
        self.current_environment_message.clear()

    def process_incoming_messages(self):
        """This function introduces control logic for dealing with messages, so that
        in the future we can use messages from other entities to help determine actions
        state etc.
        The data_ID for sender is an iteger, and we only care about the first digit. That
        is why there is some unique int(str(message['sender'])[:1]) comparission. We must first
        create a string so that we can easily slice the number up. Then we have to convert it back
        into an integer to make it more easy to work with. I will use this until a better method is
        found.
        """
        while self.messages:
            for key, value in self.messages.copy().items():
                if int(str(value['sender'])[:1]) == 3:
                    self.current_flower_message = value
                    del self.messages[key]
                if int(str(value['sender'])[:1]) == 2:
                    self.current_bee_message = value
                    del self.messages[key]
                if int(str(value['sender'])[:1]) == 4:
                    # print('Inside Flower {id} INCOMING: '.format(id=self.id),value)
                    self.current_environment_message = value
                    del self.messages[key]

    def process_current_messages(self):
        self.current_environment_temperature = self.current_environment_message['message']
        # print('Flower ',self.id,'TEMP: ',self.current_environment_temperature)

    def update(self):
        self.state.action(self.current_environment_temperature)
        if self.current_environment_temperature <= 32:
            self.notify(self.create_message(self.id, 'bee', self.state.state_id, ))
