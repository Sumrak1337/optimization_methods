import numpy as np
from methods.abstract_method import AbstractMethod


class GoldenRatio(AbstractMethod):
    def __init__(self, f=lambda x: x + 2 / x, a=0.5, b=3.5, epsilon=0.5):
        super().__init__(f=f, a=a, b=b, epsilon=epsilon)

    def get_min(self):
        gr1 = (3 - np.sqrt(5)) / 2
        gr2 = (np.sqrt(5) - 1) / 2

        a_i = self.a
        b_i = self.b
        c_i = gr1 * (b_i - a_i) + a_i
        d_i = gr2 * (b_i - a_i) + a_i
        fc = self.f(c_i)
        fd = self.f(d_i)
        self.iteration += 2

        while (b_i - a_i) / 2 > self.epsilon:
            if fc > fd:
                a_i = c_i
                c_i = d_i
                d_i = gr2 * (b_i - a_i) + a_i
                fc = fd
                fd = self.f(d_i)
                self.iteration += 1
            else:
                b_i = d_i
                d_i = c_i
                c_i = gr1 * (b_i - a_i) + a_i
                fd = fc
                fc = self.f(c_i)
                self.iteration += 1

        self.x_opt = (b_i + a_i) / 2
        self.f_opt = self.f(self.x_opt)
