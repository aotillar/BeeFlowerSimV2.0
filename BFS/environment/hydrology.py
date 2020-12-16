from scipy.interpolate import Rbf
import numpy as np
import itertools
from BFS.simulation.entity import WorldEntity


class HydrologyModel(WorldEntity):
    newid = itertools.count(4002)

    def __init__(self, name, mediator):
        super().__init__(name, mediator)
        self.name = name
        self.mediator = mediator
        self.id = next(HydrologyModel.newid)

    def notify(self, event, message):
        # print(self.id,self.name, ": >>> Out >>> : ", message)
        self.mediator.notify(event, message)

    def receive(self, message):
        print(self.name, ": <<< In <<< : ", message)


    @staticmethod
    def tcf_monthly_temperature(x):
        """
        Temperate Deciduous Forest: Temperature
        :param x: Numerical month 1-12
        :return: average daily temperature in C
        """
        return 14.1868687 - 11.0438844 * x + 4.4532585 * x ** 2 - 0.5043868 * x ** 3 + 0.0171183 * x ** 4

    @staticmethod
    def tcf_monthly_precipitation(x):
        """
        Temperate Deciduous Forest: Precipitation
        :param x: Numerical month 1-12
        :return: average daily precipitation in mm
        """
        return -3.554318e+02 + 9.461590e+02 * x - 8.375958e+02 * x ** 2 + 3.640662e+02 * x ** 3\
               - 8.735626e+01 * x ** 4 + 1.214157e+01 * x ** 5 - 9.741451e-01 * x ** 6 + 4.191430e-02 * x ** 7 \
               - 7.495953e-04 * x ** 8

    @staticmethod
    def interpolate(width, height, point_number, month_number, standard_deviation, tp_function,
                    interpolation_function='multiquadric'):
        """
        interpolate(0,100,100,1,6)
        :param interpolation_function: hat type of interpolation is desired from scipy.interpolate.rbf
        :param width: Lower bound of the interpolation
        :param height: Upper Bound of the interpolation
        :param point_number: How many data points there will be to interpolate from
        :param month_number: Month represented as a number 1-12
        :param standard_deviation: How far above or below the precipitation model
        :param tp_function: Which Temperature or Precipitation equation will be used
        'multiquadric': sqrt((r/self.epsilon)**2 + 1)
        'inverse': 1.0/sqrt((r/self.epsilon)**2 + 1)
        'gaussian': exp(-(r/self.epsilon)**2)
        'linear': r
        'cubic': r**3
        'quintic': r**5
        'thin_plate': r**2 * log(r)
        :return: ndarray object with interpolated predictions of precipitation.
        """
        width = width
        height = height
        point_number = point_number

        # -- Initialize an array with random points between width and height of size point number
        xs = np.random.uniform(width, height, point_number)
        ys = np.random.uniform(width, height, point_number)
        # -- Create temperatures associated with each of those points following a polynomial
        # -- model created from biome specific data.
        zs = np.random.normal(tp_function(month_number), standard_deviation, point_number)

        # -- Setup a grid onto which RBF will interpolate onto.
        ti = np.linspace(width, height, point_number)
        xx, yy = np.meshgrid(ti, ti)
        # -- This is where the interpolation takes place
        rbf = Rbf(xs, ys, zs, function=interpolation_function)
        # --
        zz = rbf(xx, yy)

        return zz
