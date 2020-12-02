from BFS.simulation.entity import WorldEntity
from BFS.simulation.state_machine import State
import itertools
import random as rn


def random_choice(low, high):
    return rn.randint(low, high)


class Bee(WorldEntity):
    newid = itertools.count(2000)

    def __init__(self, mediator, name):
        super().__init__(mediator, name)
        self.id = next(Bee.newid)
        self.name = name
        self.state = State()
        self.mediator = mediator
        self.messages = dict()
        self.current_flower_message = None
        self.current_bee_message = None
        self.current_environment_message = None
        self.current_environment_temperature = rn.randint(18,74)

        self.flower_messages = []
        self.bee_messages = []
        self.environment_messages = []

    def notify(self, message):
        print(self.name, ": >>> Out >>> : ", message)
        self.mediator.notify(message, self)

    def receive(self, message):
        message_id = 0
        # print(self.name, ": <<< In <<< : ", message)
        self.messages[message_id] = message
        message_id += 1

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
                    self.current_environment_message = value
                    del self.messages[key]

    def process_current_messages(self):
        self.current_environment_temperature = self.current_environment_message['message']
        print('Bee',self.id,self.current_environment_temperature)
        self.messages.clear()

    def update(self):
        self.state.action(self.current_environment_temperature)
        self.process_incoming_messages()
        self.process_current_messages()
        if self.current_environment_temperature <= 32:
            self.notify(self.create_message(self.id, 'bee', self.state.state_id, ))
