from BFS.simulation import mediator, bee , flower


class App:
    def __init__(self):
        self.entities = []
        self.mdr = mediator.Mediator()

    def initialize(self):
        self.create_bees(5)
        self.create_flowers(5)
        for ENTITY in self.entities:
            self.mdr.add(ENTITY)

    def create_bees(self,bee_number):
        for i in range(0, bee_number):
            x = bee.Bee(self.mdr, 'Bee {number}'.format(number=i))
            self.entities.append(x)

    def create_flowers(self,flower_number):
        for i in range(0, flower_number):
            x = flower.Flower(self.mdr, 'Flower {number}'.format(number=i))
            self.entities.append(x)

    def main_loop(self):
        self.initialize()

        x = 0
        while x == 0:
            for ENTITY in self.entities:
                ENTITY.update()


app = App()

if __name__ == '__main__':
    app.main_loop()
