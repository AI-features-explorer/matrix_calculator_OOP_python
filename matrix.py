import numpy as np


class MatrixError(Exception):
    """Basic exception class for matrices"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class DimensionError(MatrixError):
    """Exception arising from matrix dimension error"""
    pass


class MultiplicationError(MatrixError):
    """Exception occurring when trying to multiply incompatible matrices"""
    pass


class DeterminantError(MatrixError):
    """Exception arising when trying to calculate the determinant of a non-square matrix"""
    pass


class Matrix:
    def __init__(self, matrix):
        self._matrix = np.array(matrix)

    def add(self, other):
        if self._matrix.shape != other._matrix.shape:
            raise DimensionError("Matrices must have the same dimensions")
        return Matrix(self._matrix + other._matrix)

    def multiply(self, other):
        if self._matrix.shape[1] != other._matrix.shape[0]:
            raise MultiplicationError("Matrices are not compatible for multiplication")
        return Matrix(np.dot(self._matrix, other._matrix))

    def multiply_by_scalar(self, scalar):
        return Matrix(self._matrix * scalar)

    def transpose(self):
        return Matrix(self._matrix.T)

    def determinant(self):
        if self._matrix.shape[0] != self._matrix.shape[1]:
            raise DeterminantError("Matrix must be square to compute determinant")
        return np.linalg.det(self._matrix)
