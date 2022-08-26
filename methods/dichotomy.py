import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Dichotomy:
    """
    @:param f - Unimodal Function
    @:param a - Left Edge
    @:param b - Right Edge
    @:param epsilon e - Tolerance
    @:param delta - Constant > 0
    """
    def __init__(self, f=lambda x: x + 2 / x, a=0.5, b=3.5, epsilon=0.5, delta=0.1):
        self.f = f
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.delta = delta

        self.x_opt = None
        self.f_opt = np.inf
        self.iteration = 0

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

    def report(self):
        if self.x_opt is None:
            raise NotImplementedError("x_opt is undefined")

        print(f"Number of function calls: {self.iteration}")
        print(f"Min function value: {self.f_opt}")
        print(f"Min x value: {self.x_opt}")

        colors = list(mcolors.TABLEAU_COLORS)
        x = np.linspace(self.a, self.b, 100)

        plt.figure()
        plt.title('Dichotomy')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.scatter(self.x_opt, self.f_opt, facecolor=colors[0], color='black', label='minimum', zorder=1)
        plt.plot(x, self.f(x), color=colors[0], label='function', zorder=0)
        plt.tight_layout()
        plt.legend()
        plt.show()
