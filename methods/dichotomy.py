import numpy as np
from methods.abstract_method import AbstractMethod


class Dichotomy(AbstractMethod):
    prefix = 'Dichotomy'

    def __init__(self, f=lambda x: x + 2 / x, a=0.5, b=3.5, epsilon=0.5, delta=0.1):
        super().__init__(f=f, a=a, b=b, epsilon=epsilon, delta=delta)

    def get_min(self):
        a_i = self.a
        b_i = self.b
        while (b_i - a_i) / 2 > self.epsilon:
            c_i = (a_i + b_i - self.delta) / 2
            d_i = (a_i + b_i + self.delta) / 2
            if np.abs(a_i - c_i) <= self.epsilon or np.abs(d_i - b_i) <= self.epsilon:
                break
            fc = self.f(c_i)
            fd = self.f(d_i)
            self.iteration += 2
            if fc > fd:
                a_i = c_i
            else:
                b_i = d_i

        self.x_opt = (a_i + b_i) / 2
        self.f_opt = self.f(self.x_opt)
