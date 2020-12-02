from BFS.simulation import mediator, bee, flower
from BFS.environment import temperature


class Ecosystem:

    def __init__(self, name: str) -> None:
        """
        This is the main simulation class. All of the entities are created here
        The instance of the mediator (message) passer lives here. The simulation loop, lives
        here. This is an attempt at compartmentalizing different types of ecosystems, so that
        different biomes can be created easily and tested within the same application.
        This is also an attempt at differentiating the code so that this simulation can
        be taken apart from the GUI and dun on its own.
        :param name: Name of the Ecosystem: Eg. Forest, Mountain
        """
        self.entities = []
        self.mdr = mediator.Mediator()
        self.name = name

        # Current Ecosystem Variables
        # Temperature Water etc

        self.day_counter = -1
        self.temperature = temperature.TemperatureModel('temperature', self.mdr)

    def initialize(self):
        """
        A Function which Initializes all of the different entities in the Simulation.
        Currently these are Bees and Flowers
        """
        self.create_bees(250)
        self.create_flowers(250)
        for ENTITY in self.entities:
            self.mdr.add(ENTITY)

        self.mdr.add(self.temperature)

    def create_bees(self, bee_number):
        """
        This is a Function which creates bees dynamically. It adds the single message mediator to
        each bee that is created so that each bee can communicate with all the entities. It then
        adds that bee to a list of entities, that is used to iterate through to update all
        the different objects in the simulation.
        :param bee_number: This is an Integer of the number of bees that will be created
        :rtype: None

        """
        for i in range(0, bee_number):
            x = bee.Bee(self.mdr, 'Bee {number}'.format(number=i))
            self.entities.append(x)

    def create_flowers(self, flower_number):
        """
        This is a Function which creates Flowers dynamically. It adds the single message mediator to
        each flower that is created so that each fl;ower can communicate with all the entities. It then
        adds that flower to a list of entities, that is used to iterate through to update all
        the different objects in the simulation.
        :param flower_number: This is an Integer of the number of flowers that will be created
        :type flower_number: int
        """
        for i in range(0, flower_number):
            x = flower.Flower(self.mdr, 'Flower {number}'.format(number=i))
            self.entities.append(x)

    def update(self) -> None:
        """
        This function takes all of the different entities, and loops through their respective functions that are
        required for the simulation logic.
        """
        self.day_counter += 1
        self.temperature.update(102.7, 65.5, 49.6, 18, self.day_counter)

        for ENTITY in self.entities:
            ENTITY.process_incoming_messages()

        for ENTITY in self.entities:
            ENTITY.process_current_messages()

        for ENTITY in self.entities:
            ENTITY.update()

        if self.day_counter > 365:
            self.day_counter = 0

        # print(self.day_counter)
        # print('*--------------------------NEW DAY------------------------------*')
        # print(' ')
