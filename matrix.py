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