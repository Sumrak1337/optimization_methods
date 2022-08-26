import numpy as np
from methods.abstract_method import AbstractMethod


class PassiveSearch(AbstractMethod):
    prefix = 'Passive Search'

    def __init__(self, f=lambda x: x + 2 / x, a=0.5, b=3.5, epsilon=0.5):
        super().__init__(f=f, a=a, b=b, epsilon=epsilon)
        self.k = int((self.b - self.a) / self.epsilon)

    def get_min(self):
        xs = np.array([self.a + (self.b - self.a) * i / self.k for i in range(self.k + 1)])
        for x in xs:
            value = self.f(x)
            self.iteration += 1
            if value < self.f_opt:
                self.f_opt = value
                self.x_opt = x
