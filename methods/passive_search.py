import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class PassiveSearch:
    """
    @:param f - Unimodal Function
    @:param a - Left Edge
    @:param b - Right Edge
    @:param epsilon e - Tolerance
    """
    def __init__(self, f=lambda x: x + 2 / x, a=0.5, b=3.5, epsilon=0.5):
        self.f = f
        self.a = a
        self.b = b
        self.epsilon = epsilon

        self.k = int((self.b - self.a) / self.epsilon)
        self.f_opt = np.inf
        self.x_opt = None
        self.iteration = 0

    def get_min(self):
        xs = np.array([self.a + (self.b - self.a) * i / self.k for i in range(self.k + 1)])
        for x in xs:
            value = self.f(x)
            self.iteration += 1
            if value < self.f_opt:
                self.f_opt = value
                self.x_opt = x

    def report(self):
        if self.x_opt is None:
            raise NotImplementedError("x_opt is undefined")
        print(f"Number of function calls: {self.iteration}")
        print(f"Min function value: {self.f_opt}")
        print(f"Min x value: {self.x_opt}")

        colors = list(mcolors.TABLEAU_COLORS)
        x = np.linspace(self.a, self.b, 100)

        plt.figure()
        plt.title('Passive Search')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.scatter(self.x_opt, self.f_opt, facecolor=colors[0], color='black', label='minimum', zorder=1)
        plt.plot(x, self.f(x), color=colors[0], label='function', zorder=0)
        plt.tight_layout()
        plt.legend()
        plt.show()
