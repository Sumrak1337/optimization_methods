import numpy as np
from methods.abstract_method import AbstractMethod


class PassiveSearch:
    prefix = 'Passive_Search'

    def __init__(self, function, epsilon):
        self.function = function
        self.k = int((self.function.ub - self.function.lb) / epsilon)

        self.iteration = 0
        self.f_opt = np.inf
        self.x_opt = None

        self.history = np.array([])

    def get_min(self):
        xs = np.array([self.function.lb + (self.function.ub - self.function.lb) * i / self.k
                       for i in range(self.k + 1)])
        for x in xs:
            value = self.function.f(x)
            self.iteration += 1
            self.history = np.append(self.history, value)
            if value < self.f_opt:
                self.f_opt = value
                self.x_opt = x
            else:
                break
