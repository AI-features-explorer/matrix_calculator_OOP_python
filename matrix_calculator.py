from matrix import Matrix


class MatrixCalculator:
    def __init__(self):
        self.matrices = []

    def add_matrix(self, matrix):
        new_matrix = Matrix(matrix)
        self.matrices.append(new_matrix)
        return new_matrix

    def remove_matrix_by_index(self, index):
        if index < 0 or index >= len(self.matrices):
            raise IndexError("Invalid matrix index")
        del self.matrices[index]

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
