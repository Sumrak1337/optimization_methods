import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class AbstractMethod:
    """
    @:param f - Unimodal Function
    @:param a - Left Edge
    @:param b - Right Edge
    @:param epsilon e - Tolerance
    @:param delta - Constant > 0
    """
    prefix = 'Abstract Method'

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
        raise NotImplementedError

    def report(self):
        if self.x_opt is None:
            raise NotImplementedError("x_opt is undefined")

        print(f"Number of function calls: {self.iteration}")
        print(f"Min function value: {self.f_opt}")
        print(f"Min x value: {self.x_opt}")

        colors = list(mcolors.TABLEAU_COLORS)
        x = np.linspace(self.a, self.b, 100)

        plt.figure()
        plt.title(f'{self.prefix}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.scatter(self.x_opt, self.f_opt, facecolor=colors[0], color='black', label='minimum', zorder=1)
        plt.plot(x, self.f(x), color=colors[0], label='function', zorder=0)
        plt.tight_layout()
        plt.legend()
        plt.show()
