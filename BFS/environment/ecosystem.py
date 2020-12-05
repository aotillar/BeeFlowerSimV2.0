from BFS.simulation import mediator, bee, flower
from BFS.environment import temperature
from BFS.environment import hydrology
import numpy as np
import datetime


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
        self.event_types = ['bee', 'flower', 'temp', 'hydrology', 'none']
        self.entities = []
        self.mdr = mediator.Mediator(self.event_types)
        self.name = name

        # Simulations Time Variables
        self.dayNumber = 0
        self.dayCounter = 0
        self.weekCounter = 0
        self.monthCounter = 0
        self.seasonCounter = 0
        self.evolveCounter = 0
        self.year = 2018
        self.date = datetime.date(self.year, 1, 1)
        self.time_step_per_day_counter = 0
        self.time_step_per_day_limit = 1

        # Current Ecosystem Models
        # Temperature Water etc

        self.year_day_counter = -1
        self.temperature = temperature.TemperatureModel('temperature', self.mdr)
        self.hydrology = hydrology.HydrologyModel('hydrology', self.mdr)

        # Current Ecosystem Variables
        self.width = 0
        self.height = 100
        self.precip_gids = dict()

    def initialize(self):
        """
        A Function which Initializes all of the different entities in the Simulation.
        Currently these are Bees and Flowers.

        This function also initializes all of the interpolated hydrology and temperature
        grids, before the simulation runs, in order to keep processing time during
        the simulation free.
        """
        # Create Entities and add them to the environment

        self.create_bees(100)
        self.create_flowers(100)

        # Register them with the Mediator/Message Interface
        for ENTITY in self.entities:
            self.mdr.register('temp', ENTITY)

        # Register the Temperature and Hydrology models with the message interface
        self.mdr.register('none', self.temperature)
        self.mdr.register('none', self.hydrology)

        # Calculate all of the monthly precipitation grids
        self.create_monthly_precipitation_girds()

    def create_monthly_precipitation_girds(self):
        for i in range(1, 13):
            grid = self.hydrology.interpolate(self.width, self.height,
                                                             100, i, 6, self.hydrology.tcf_monthly_precipitation)
            grid[grid<0] = 0
            self.precip_gids[i] = grid

    def register_for_bee_events(self):
        pass

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
            x = np.random.randint(0, self.height)
            y = np.random.randint(0, self.height)
            x = bee.Bee(self.mdr, 'Bee {number}'.format(number=i),x,y)
            self.mdr.register('bee', x)
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
            x = np.random.randint(0,self.height)
            y = np.random.randint(0, self.height)
            x = flower.Flower(self.mdr, 'Flower {number}'.format(number=i),x,y)
            self.mdr.register('flower', x)
            self.entities.append(x)

    def update_time_counters(self):
        self.year_day_counter += 1
        self.monthCounter = datetime.date(self.year, 1, 1) + datetime.timedelta(self.year_day_counter)
        if self.year_day_counter > 365:
            self.year_day_counter = 0

    def update(self) -> None:
        """
        This function takes all of the different entities, and loops through their respective functions that are
        required for the simulation logic.
        """

        self.temperature.update(102.7, 65.5, 49.6, 18, self.year_day_counter)
        self.update_time_counters()

        for ENTITY in self.entities:
            ENTITY.process_incoming_messages()

        for ENTITY in self.entities:
            ENTITY.process_current_messages()

        for ENTITY in self.entities:
            ENTITY.poll_precipitation(self.precip_gids[self.monthCounter.month])

        for ENTITY in self.entities:
            ENTITY.update()






        # print(self.day_counter)
        # print('*--------------------------NEW DAY------------------------------*')
        # print(' ')

if __name__ == '__main__':
    e = Ecosystem('e')
    for i in range(365):
        e.update()
