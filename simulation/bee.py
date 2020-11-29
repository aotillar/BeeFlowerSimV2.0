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
        self.messages = []
        self.current_flower_message = None
        self.current_bee_message = None
        self.current_environment_message = None

    def notify(self, message):
        print(self.name, ": >>> Out >>> : ", message)
        self.mediator.notify(message, self)

    def receive(self, message):
        print(self.name, ": <<< In <<< : ", message)
        self.messages.append(message)

    def process_messages(self):
        """This function introduces control logic for dealing with messages, so that
        in the future we can use messages from other entities to help determine actions
        state etc.
        The data_ID for sender is an iteger, and we only care about the first digit. That
        is why there is some unique int(str(message['sender'])[:1]) comparission. We must first
        create a string so that we can easily slice the number up. Then we have to convert it back
        into an integer to make it more easy to work with. I will use this until a better method is
        found.
        """
        for message in self.messages:
            if int(str(message['sender'])) == self.id:
                self.messages.remove(message)
            if int(str(message['sender'])[:1]) == 3 and message['receiver'] == 'bee':
                print('I recieved a message from flowers')
                self.current_flower_message = self.messages.remove(message)
            if int(str(message['sender'])[:1]) == 4 and message['receiver'] == 'all':
                print('I recieved a message from environment')
                self.current_environment_message = self.messages.remove(message)

    def update(self):
        self.state.action(1)
        self.process_messages()
        self.notify(self.create_message(self.id, 'bee', self.state.state_id, ))
