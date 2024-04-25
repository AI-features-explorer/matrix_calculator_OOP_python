import numpy as np

class MatrixError(Exception):
    """Basic exception class for matrices"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)