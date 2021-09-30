"""Relationship between the eigenDecomposition and singular values."""

import numpy as np

"""
Case1: eig(A'A) == svd(A)
"""


def case1(matrix):
    eig = np.sort(np.linalg.eig(matrix.T @ matrix)[0])
    svd = np.sort(np.linalg.svd(matrix[1])) ** 2

    return eig, svd


"""
case2: eig(A'A) == svd(A'A)
"""


def case2(matrix):
    eig = np.sort(np.linalg.eig(matrix.T @ matrix)[0])
    svd = np.sort(np.linalg.svd(matrix.T @ matrix)[1])

    return eig, svd


"""
case3: eig(A) vs svd(A), for real-valued eigen and complex eigen.
"""


def case3a(matrix):
    eig = np.sort(np.linalg.eig(matrix)[0])
    svd = np.sort(np.linalg.svd(matrix)[1])

    return eig, svd
