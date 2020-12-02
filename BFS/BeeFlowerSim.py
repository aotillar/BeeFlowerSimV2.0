from BFS.environment import ecosystem
import time


class App:
    def __init__(self):
        self.current_environment = ecosystem.Ecosystem('forest')

    def main_loop(self):
        tin = time.perf_counter()
        self.current_environment.initialize()

        x = 0
        while x <= 365:
            self.current_environment.update()
            x += 1
        tout = time.perf_counter()
        print('Total Program Execution:', tout - tin)


app = App()

if __name__ == '__main__':
    import cProfile
    #
    cProfile.run('app.main_loop()')
    # app.main_loop()
