import numpy as np
from methods.abstract_method import AbstractMethod


class Dichotomy:
    prefix = 'Dichotomy'

    def __init__(self, function, epsilon=0.5, delta=0.1):
        self.function = function
        self.epsilon = epsilon
        self.delta = delta

        self.iteration = 0
        self.f_opt = np.inf
        self.x_opt = None

        self.history = np.array([])

    def get_min(self):
        a_i = self.function.lb
        b_i = self.function.ub
        while (b_i - a_i) / 2 > self.epsilon:
            c_i = (a_i + b_i - self.delta) / 2
            d_i = (a_i + b_i + self.delta) / 2
            if np.abs(a_i - c_i) <= self.epsilon or np.abs(d_i - b_i) <= self.epsilon:
                break
            fc = self.function.f(c_i)
            fd = self.function.f(d_i)
            self.iteration += 2
            if fc > fd:
                a_i = c_i
                self.history = np.append(self.history, fd)
            else:
                b_i = d_i
                self.history = np.append(self.history, fc)

        self.x_opt = (a_i + b_i) / 2
        self.f_opt = self.function.f(self.x_opt)
