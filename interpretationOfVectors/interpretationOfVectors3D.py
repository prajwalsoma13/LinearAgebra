import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def interpretation3D(vector):
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = fig.gca(projection='3d')
    ax.plot([0, vector[0]], [0, vector[1]], [0, vector[2]], linewidth=3)

    ax.plot([0, 0], [0, 0], [-4, 4], color='k', linestyle='--')
    ax.plot([0, 0], [-4, 4], [0, 0], color='k', linestyle='--')
    ax.plot([-4, 4], [0, 0], [0, 0], color='k', linestyle='--')
    plt.show()


"""3D vectorAdditionNSubtraction"""
v1 = [3, -2, 5]
interpretation3D(v1)
