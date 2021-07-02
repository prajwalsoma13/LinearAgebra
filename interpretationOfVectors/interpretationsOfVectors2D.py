import numpy as np
import matplotlib.pyplot as plt


def interpretation2D(vector):
    plt.plot([0, vector[0]], [0, vector[1]])
    plt.axis('equal')
    plt.plot([-4, 4], [0, 0], color='k', linestyle='--')
    plt.plot([0, 0], [-4, 4], color='k', linestyle='--')
    plt.grid()
    plt.axis((-4, 4, -4, 4))
    plt.show()


"""2D vectorAdditionNSubtraction"""
v1 = [3, -2]
interpretation2D(v1)
