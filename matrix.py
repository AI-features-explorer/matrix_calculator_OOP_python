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
        self.__matrix = np.array(matrix)

    @property
    def current(self):
        return self.__matrix

    def multiply(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The 'other' argument must be a Matrix object")
        if self.current.shape[1] != other.current.shape[0]:
            raise MultiplicationError("Matrices are not compatible for multiplication")
        return Matrix(np.dot(self.current, other.current))

    def add(self, other):
        if self.current.shape != other.current.shape:
            raise DimensionError("Matrices must have the same dimensions")
        return Matrix(self.current + other.current)

    def multiply_by_scalar(self, scalar):
        return Matrix(self.current * scalar)

    def transpose(self):
        return Matrix(self.current.T)

    def determinant(self):
        if self.current.shape[0] != self.current.shape[1]:
            raise DeterminantError("Matrix must be square to compute determinant")
        return np.linalg.det(self.current)
