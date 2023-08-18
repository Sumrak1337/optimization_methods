import numpy as np


class AbstractFunction:
    def f(self, x):
        raise NotImplementedError


class F1(AbstractFunction):
    prefix = r'$ax^2 + bx + c$'

    def __init__(self, seed):

        rs = np.random.RandomState(seed)
        self.lb, self.ub = -5, 5
        self.a, self.b, self.c = (self.ub - self.lb) * rs.random(3) + self.lb
        self.a = np.abs(self.a)

        self.x_min = -self.b / self.a / 2
        self.f_min = self.f(self.x_min)

    def f(self, x):
        return self.a * x ** 2 + self.b * x + self.c


class F2(AbstractFunction):
    prefix = r'$x^n + \frac{n}{x}$'

    def __init__(self, seed):

        rs = np.random.RandomState(seed)
        self.degree = rs.randint(1, 5)
        self.lb, self.ub = 0.1, 3

        self.x_min = 1
        self.f_min = self.f(self.x_min)

    def f(self, x):
        return x ** self.degree + self.degree / x
