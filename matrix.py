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
        self.matrix = np.array(matrix)

    def add(self, other):
        if self.matrix.shape != other.matrix.shape:
            raise DimensionError("Matrices must have the same dimensions")
        return Matrix(self.matrix + other.matrix)

    def multiply(self, other):
        if self.matrix.shape[1] != other.matrix.shape[0]:
            raise MultiplicationError("Matrices are not compatible for multiplication")
        return Matrix(np.dot(self.matrix, other.matrix))

    def multiply_by_scalar(self, scalar):
        return Matrix(self.matrix * scalar)

    def transpose(self):
        return Matrix(self.matrix.T)

    def determinant(self):
        if self.matrix.shape[0] != self.matrix.shape[1]:
            raise DeterminantError("Matrix must be square to compute determinant")
        return np.linalg.det(self.matrix)
