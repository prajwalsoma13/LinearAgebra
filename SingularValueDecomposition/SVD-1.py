"""Computing singular value decomposition"""

import numpy as np
import matplotlib.pyplot as plt


def findSVD(matrix):
    """
    :param matrix: Input can be either square or rectangular matrix.
    :return: The SVD of a matrix i.e (U: orthogonal basis for column space input matrix,
                                      S: Singular values of input matrix,
                                      V: orthogonal basis for row space input matrix)
    """

    U, S, V = np.linalg.svd(matrix)

    return U, S, V


def plotValues(subPlotValue, values, pltTitle, axisPlt):
    plt.subplot(subPlotValue)
    plt.imshow(values)
    plt.title(pltTitle)
    plt.axis(axisPlt)


"""Consider a square/rectangular matrix"""
A = [[3, 0, 5],
     [8, 1, 3]]

valueU, valueS, valueV = findSVD(A)

plotValues(141, A, 'A', 'off')
plotValues(142, valueU, 'U', 'off')
plotValues(143, np.diag(valueS), '$\Sigma$', 'off')
plotValues(144, valueV, '$V^T$', 'off')

plt.show()
