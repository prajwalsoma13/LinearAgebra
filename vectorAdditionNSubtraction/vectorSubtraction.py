import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def vectorSubtraction(vector1, vector2):
    vector3 = vector1 - vector2

    plt.plot([0, vector1[0]], [0, vector1[1]], color='b', label='v1')
    plt.plot([0, vector2[0]], [0, vector2[1]], color='r', label='v2')
    plt.plot([0, vector3[0]], [0, vector3[1]], color='k', label='v1 - v2')

    plt.legend()
    plt.axis('square')
    plt.axis((-6, 6, -6, 6))
    plt.grid()
    plt.show()


v1 = np.array([3, -1])
v2 = np.array([2, 4])

vectorSubtraction(v1, v2)
