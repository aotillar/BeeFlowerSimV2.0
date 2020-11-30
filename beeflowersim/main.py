from BFS.environment import ecosystem


class App:
    def __init__(self):
        self.current_environment = ecosystem.Ecosystem('forest')

    def main_loop(self):
        self.current_environment.initialize()

        x = 0
        while x <= 3:
            self.current_environment.update()
            x += 1



app = App()

if __name__ == '__main__':
    app.main_loop()
