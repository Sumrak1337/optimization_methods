import numpy as np
from methods.abstract_method import AbstractMethod


class Secant(AbstractMethod):
    def __init__(self, f=lambda x: x + 2 / x, a=0.5, b=3.5, epsilon=0.5):
        super().__init__(f=f, a=a, b=b, epsilon=epsilon)

    def get_min(self):
        a_i = self.a
        b_i = self.b
        fa = self.f(a_i)
        fb = self.f(b_i)
        self.iteration += 2
        while np.abs(b_i - a_i) > self.epsilon:
            x, y = self.get_intersection_point(a_i, b_i, fa, fb)
            der_x = self.get_der(x)
            if der_x < 0:
                a_i = x
                fa = self.f(x)
            else:
                b_i = x
                fb = self.f(x)
            self.iteration += 1

        self.x_opt = (a_i + b_i) / 2
        self.f_opt = self.f(self.x_opt)

    def get_der(self, x0):
        dx = 1e-10
        self.iteration += 2
        return (self.f(x0 + dx) - self.f(x0)) / dx

    def get_intersection_point(self, a_i, b_i, fa, fb):
        k1 = self.get_der(a_i)
        k2 = self.get_der(b_i)
        b1 = fa - k1 * a_i
        b2 = fb - k2 * b_i
        # TODO: add exception with k1 == k2
        x = (b2 - b1) / (k1 - k2)
        y = (k1 * b2 + b1 * k2) / (k1 - k2)
        return x, y
