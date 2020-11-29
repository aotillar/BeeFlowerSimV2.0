from BFS.simulation import mediator, bee, flower
from BFS.environment import temperature


class Ecosystem:

    def __init__(self, name):
        self.entities = []
        self.mdr = mediator.Mediator()
        self.name = name
        # Current Ecosystem Variables
        # Temperature Water etc
        self.day_counter = 0
        self.temperature = temperature.TemperatureModel('temperature', self.mdr)

    def initialize(self):
        self.create_bees(5)
        self.create_flowers(5)
        for ENTITY in self.entities:
            self.mdr.add(ENTITY)

        self.mdr.add(self.temperature)

    def create_bees(self, bee_number):
        for i in range(0, bee_number):
            x = bee.Bee(self.mdr, 'Bee {number}'.format(number=i))
            self.entities.append(x)

    def create_flowers(self, flower_number):
        for i in range(0, flower_number):
            x = flower.Flower(self.mdr, 'Flower {number}'.format(number=i))
            self.entities.append(x)

    def update(self):
        self.day_counter += 0

        self.temperature.update(102.7, 65.5, 49.6, 18, self.day_counter)

        for ENTITY in self.entities:
            ENTITY.update()

        if self.day_counter >= 365:
            self.day_counter = 0
