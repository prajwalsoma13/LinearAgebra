"""U from eigenDecomposition of A"""
import numpy as np


def eigenDecomposition(matrix):
    """
    :param matrix: Input can only be square matrix.
    :return: The eigen elements of a matrix i.e (L: eigen values,
                                                 W: eigen vectors)
    """
    L, W = np.linalg.eig(matrix)
    return L, W


def findSVD(matrix):
    """
    :param matrix: Input can be either square or rectangular matrix.
    :return: The SVD of a matrix i.e (U: orthogonal basis for column space input matrix,
                                      S: Singular values of input matrix,
                                      V: orthogonal basis for row space input matrix)
    """

    U, S, V = np.linalg.svd(matrix)
    return U, S, V


"""create a matrix of (3x6)"""
m = 3
n = 6
A = np.random.randn(m, n)
symmetricA = A.T @ A

eigenValues, eigenVectors = eigenDecomposition(symmetricA)
valueU, valueS, valueV = findSVD(A)

"""Sorting eigenDecomposition Values."""
sidx = np.argsort(eigenValues)[::-1]
eigenValues = eigenValues[sidx]
eigenVectors = eigenVectors[:, sidx]

"""confirm that eigenVectors == right singular vectors"""
print(np.round(valueV.T+eigenVectors, 2))


"""check the relationship between singularValues and eigenValues"""
print(eigenValues)
print(valueS**2)

"""Create U using only A, V, L"""


def createU(matrix, matrixA, svdU, eigL):
    U = np.zeros((matrix, matrix))
    for i in range(m):
        U[:, i] = matrixA@eigenVectors[:, i].T/np.sqrt(eigL[i])

    return np.round(U - svdU, 2)


result = createU(m, A, valueU, eigenValues)
print(result)
