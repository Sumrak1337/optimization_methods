import numpy as np
from methods.abstract_method import AbstractMethod


class Fibonacci(AbstractMethod):
    def __init__(self, f=lambda x: x + 2 / x, a=0.5, b=3.5, epsilon=0.5):
        super().__init__(f=f, a=a, b=b, epsilon=epsilon)
        self.fib_list = np.array([])
        self.fib_n = int(np.ceil((self.b - self.a) / self.epsilon))
        self.fibonacci(self.fib_n)

        self.n = (np.where(self.fib_list >= self.fib_n)[0] - 2)[0]

    def get_min(self):
        a_i = self.a
        b_i = self.b
        c_i = a_i + (b_i - a_i) * self.fib_list[self.n] / self.fib_list[self.n + 2]
        d_i = a_i + (b_i - a_i) * self.fib_list[self.n + 1] / self.fib_list[self.n + 2]
        fc = self.f(c_i)
        fd = self.f(d_i)
        self.iteration += 2

        for i in range(1, self.n + 1):
            if fc < fd:
                b_i = d_i
                d_i = c_i
                c_i = a_i + (b_i - a_i) * self.fib_list[self.n - i] / self.fib_list[self.n + 2 - i]
                fd = fc
                if i != self.n:
                    fc = self.f(c_i)
                    self.iteration += 1
            else:
                a_i = c_i
                c_i = d_i
                d_i = a_i + (b_i - a_i) * self.fib_list[self.n + 1 - i] / self.fib_list[self.n + 2 - i]
                fc = fd
                if i != self.n:
                    fd = self.f(d_i)
                    self.iteration += 1

        self.x_opt = (b_i + a_i) / 2
        self.f_opt = self.f(self.x_opt)

    def fibonacci(self, n):
        for i in range(n):
            if (i == 0) or (i == 1):
                self.fib_list = np.append(self.fib_list, 1)
            else:
                value = self.fib_list[i - 1] + self.fib_list[i - 2]
                self.fib_list = np.append(self.fib_list, value)
                if value > self.fib_n:
                    break
