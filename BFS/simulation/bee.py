from BFS.simulation.entity import WorldEntity
from BFS.simulation.state_machine import State
import itertools
from operator import itemgetter
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
        self.messages = []
        self.current_flower_message = None
        self.current_bee_message = None
        self.current_environment_message = None
        self.current_environment_temperature = None

    def notify(self, message):
        # print(self.name, ": >>> Out >>> : ", message)
        self.mediator.notify(message, self)

    def receive(self, message):
        # print(self.name, ": <<< In <<< : ", message)
        if message['receiver'] == 'bee' or message['receiver'] == 'all':
            self.messages.append(message)

    def clear_messages(self):
        self.messages.clear()

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
        flower_messages = []
        bee_messages = []
        environment_messages = []
        # print('    BEE LENGTH OF SELF.MESSAGES',len(self.messages))
        while self.messages:
            for message in self.messages:
                # print('    BEE PROCESS: SENDER NUMBER ID',int(str(message['sender'])))
                if int(str(message['sender'])) == self.id:
                    # print('            1B REMOVED A MESSAGE')
                    self.messages.remove(message)
                if int(str(message['sender'])[:1]) == 3 and message in self.messages:
                    flower_messages.append(message)
                    self.messages.remove(message)
                    # print('            2B REMOVED A MESSAGE')
                if int(str(message['sender'])[:1]) == 2 and message in self.messages:
                    bee_messages.append(message)
                    self.messages.remove(message)
                    # print('            3B REMOVED A MESSAGE')
                if int(str(message['sender'])) == 4001 and message in self.messages:
                    environment_messages.append(message)
                    # print('    INSIDE IF',environment_messages)
                    # print('    B        Added and Environment message')
                    self.messages.remove(message)
                    # print('            4B REMOVED A MESSAGE')

        # print('BEE ENVIRONMENT MESSAGES BEFORE SORT', environment_messages)
        # print('BEE FLOWER MESSAGES BEFORE SORT', bee_messages)
        # print('BEE MESSAGES BEFORE SORT', flower_messages)
        # print(' ')
        flower_messages = sorted(flower_messages, key=itemgetter('time'))
        if flower_messages:
            # print('FM',True)
            self.current_flower_message = flower_messages.pop()
        bee_messages = sorted(bee_messages, key=itemgetter('time'))
        if bee_messages:
            # print('BM',True)
            self.current_bee_message = bee_messages.pop()
        environment_messages = sorted(environment_messages, key=itemgetter('time'))
        if environment_messages:
            # print('EM',True)
            self.current_environment_message = environment_messages.pop()
        #     print('INSIDE EM', self.current_environment_message)
        # print('BEE ENVIRONMENT MESSAGES AFTER SORT', environment_messages)
        # print('BEE MESSAGES AFTER SORT', bee_messages)
        # print('BEE MESSAGES AFTER SORT', flower_messages)
        self.current_environment_temperature = self.current_environment_message['message']
        self.messages.clear()

    def update(self):
        self.state.action(1)
        self.process_messages()
        # print('BEE CURRENT TEMP',self.current_environment_temperature)
        # print('*****-----**END OF BEE UPDATE**-----*****')
        if self.current_environment_temperature <= 32:
            self.notify(self.create_message(self.id, 'flower', self.state.state_id, ))
