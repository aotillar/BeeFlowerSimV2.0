import numpy as np
import itertools
from BFS.simulation.entity import WorldEntity


class TemperatureModel(WorldEntity):
    newid = itertools.count(4001)

    def __init__(self, name, mediator):
        super().__init__(name, mediator)
        self.name = name
        self.mediator = mediator
        self.id = next(TemperatureModel.newid)
        self.current_temperature = 0

    def notify(self, event, message):
        # print(self.id,self.name, ": >>> Out >>> : ", message)
        self.mediator.notify(event, message)

    def receive(self, message):
        print(self.name, ": <<< In <<< : ", message)

    @staticmethod
    def temp_north_day_high(thigh, tlow, day):
        """This function uses a trigonometric function and transposes it
        to fit the thigh, tlow. This model assumes that temperature changes
        uniformly throughout the year according to a standard wave function.
        Once the function is transposed, it then uses day as an x variable
        to get the according y value(temperature) for that particular day"""
        x = np.linspace(0, 366, 366)
        a = (thigh - tlow) / 2
        d = (thigh + tlow) / 2
        y = a * np.cos((2 * np.pi / 365) * (x - 182.5)) + d
        if day:
            return y[day]
        if day == 0:
            return y[1]
        else:
            return y

    @staticmethod
    def temp_north_day_low(thigh, tlow, day):
        x = np.linspace(0, 366, 366)
        a = (thigh - tlow) / 2
        d = (thigh + tlow) / 2
        y = a * np.cos((2 * np.pi / 365) * (x - 182.5)) + d
        if day:
            return y[day]
        if day == 0:
            return y[1]
        else:
            return y

    @staticmethod
    def temp_south_day_high(thigh, tlow, day=None):
        x = np.linspace(0, 366, 366)
        a = (thigh - tlow) / 2
        d = (thigh + tlow) / 2
        y = a * -np.cos((2 * np.pi / 365) * (x - 182.5)) + d
        if day:
            return y[day]
        else:
            return y

    @staticmethod
    def temp_south_day_low(thigh, tlow, day=None):
        x = np.linspace(0, 366, 366)
        a = (thigh - tlow) / 2
        d = (thigh + tlow) / 2
        y = a * -np.cos((2 * np.pi / 365) * (x - 182.5)) + d
        if day:
            return y[day]
        else:
            return y

    @staticmethod
    def temp_hour(thigh, tlow, hour=None):
        """This function uses a trigonometric function and transposes it
            to fit the thigh, tlow. This model assumes that temperature changes
            uniformly throughout the year according to a standard wave function.
            Once the function is transposed, it then uses hour as an x variable
            to get the according y value(temperature) for that particular hour"""
        x = np.linspace(0, 24, 24)
        a = (thigh - tlow) / 2
        d = (thigh + tlow) / 2
        y = a * np.cos((2 * np.pi / 24) * (x - 182.5)) + d
        return y[hour]

    def random_daily_temperature(self, high_lrg, high_lw, low_lrg, low_lw, day):
        """High and Low values are for Yearly All Time high, and Yearly all time low.
        This function assumes a bell curve for yearly average temperature."""
        y1 = self.temp_north_day_high(high_lrg, high_lw, day)
        y2 = self.temp_north_day_low(low_lrg, low_lw, day)
        y_average = (y1 + y2) / 2
        return np.random.normal(y_average, 10)

    def update(self, high_lrg, high_lw, low_lrg, low_lw, day):

        dail_temperature = self.random_daily_temperature(high_lrg, high_lw, low_lrg, low_lw, day)
        self.current_temperature = dail_temperature
        daily_temp_message = self.create_message(self.id, 'all', dail_temperature)
        self.notify('temp', daily_temp_message)
        # return daily_temp_message
