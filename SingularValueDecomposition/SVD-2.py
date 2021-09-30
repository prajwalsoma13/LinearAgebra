"""Relationship between eigenValues and SVD for symmetric matrix."""
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


def eigenDecomposition(matrix):
    """
    :param matrix: Input can only be square matrix.
    :return: The eigen elements of a matrix i.e (L: eigen values,
                                                 W: eigen vectors)
    """
    L, W = np.linalg.eig(matrix)
    return L, W


def plotValues(ax, value1, value2, value3, title1, title2, title3, rowValue):
    ax[rowValue, 0].imshow(value1)
    ax[rowValue, 0].set_title(title1)
    ax[rowValue, 1].imshow(value2)
    ax[rowValue, 1].set_title(title2)
    ax[rowValue, 2].imshow(value3)
    ax[rowValue, 2].set_title(title3)


"""Create a symmetric matrix(5x5)"""
A = np.random.rand(5, 5)
symmetricA = A.T @ A

eigenValues, eigenVectors = eigenDecomposition(symmetricA)
valueU, valueS, valueV = findSVD(A)

"""Sorting eigenDecomposition Values."""
sidx = np.argsort(eigenValues)[::-1]
eigenValues = eigenValues[sidx]
eigenVectors = eigenVectors[:, sidx]

fig, ax = plt.subplots(2, 3, figsize=(10, 7))
plotValues(ax, eigenVectors, np.diag(eigenValues), np.zeros((1, 1,)), 'W (eig)', 'L (eig)', 'Zeros', 0)
plotValues(ax, valueU, np.diag(valueS), valueV, 'U', '$\Sigma$', '$V^T$', 1)

plt.show()
