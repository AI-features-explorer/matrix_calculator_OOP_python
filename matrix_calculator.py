from matrix import Matrix, DimensionError, MultiplicationError, DeterminantError


class MatrixCalculator:
    def __init__(self):
        self.matrices = []

    def add_matrix(self, matrix):
        new_matrix = Matrix(matrix)
        self.matrices.append(new_matrix)
        return new_matrix

    def perform_operation(self, operation, *args):
        if operation == "add":
            return self.matrices[args[0]].add(self.matrices[args[1]])
        elif operation == "multiply":
            return self.matrices[args[0]].multiply(self.matrices[args[1]])
        elif operation == "multiply_by_scalar":
            return self.matrices[args[0]].multiply_by_scalar(args[1])
        elif operation == "transpose":
            return self.matrices[args[0]].transpose()
        elif operation == "determinant":
            return self.matrices[args[0]].determinant()
        else:
            raise ValueError("Unsupported operation")
