import unittest
import numpy as np
from matrix import Matrix, DimensionError, MultiplicationError, DeterminantError
from matrix_calculator import MatrixCalculator


class TestMatrix(unittest.TestCase):

    def test_add(self):
        mat1 = Matrix([[1, 2], [3, 4]])
        mat2 = Matrix([[5, 6], [7, 8]])
        result = mat1.add(mat2)
        expected = np.array([[6, 8], [10, 12]])
        np.testing.assert_array_equal(result.current_matrix, expected)

    def test_add_dimension_error(self):
        mat1 = Matrix([[1, 2], [3, 4]])
        mat2 = Matrix([[5, 6]])
        with self.assertRaises(DimensionError):
            mat1.add(mat2)

    def test_multiply(self):
        mat1 = Matrix([[1, 2], [3, 4]])
        mat2 = Matrix([[2], [1]])
        result = mat1.multiply(mat2)
        expected = np.array([[4], [10]])
        np.testing.assert_array_equal(result.current_matrix, expected)

    def test_multiply_multiplication_error(self):
        mat1 = Matrix([[1, 2], [3, 4]])
        mat2 = Matrix([[2, 3]])
        with self.assertRaises(MultiplicationError):
            mat1.multiply(mat2)

    def test_multiply_by_scalar(self):
        mat = Matrix([[1, 2], [3, 4]])
        result = mat.multiply_by_scalar(2)
        expected = np.array([[2, 4], [6, 8]])
        np.testing.assert_array_equal(result.current_matrix, expected)

    def test_transpose(self):
        mat = Matrix([[1, 2], [3, 4], [5, 6]])
        result = mat.transpose()
        expected = np.array([[1, 3, 5], [2, 4, 6]])
        np.testing.assert_array_equal(result.current_matrix, expected)

    def test_determinant(self):
        mat = Matrix([[4, 7], [2, 6]])
        result = mat.determinant()
        self.assertAlmostEqual(result, 10)

    def test_determinant_error(self):
        mat = Matrix([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(DeterminantError):
            mat.determinant()


class TestMatrixCalculator(unittest.TestCase):

    def test_add_matrix(self):
        calc = MatrixCalculator()
        mat = [[1, 2], [3, 4]]
        result = calc.add_matrix(mat)
        expected = Matrix(mat)
        np.testing.assert_array_equal(result.current_matrix, expected.current_matrix)

    def test_perform_operation_add(self):
        calc = MatrixCalculator()
        mat1 = calc.add_matrix([[1, 2], [3, 4]])
        mat2 = calc.add_matrix([[5, 6], [7, 8]])
        result = calc.perform_operation("add", 0, 1)
        expected = np.array([[6, 8], [10, 12]])
        np.testing.assert_array_equal(result.current_matrix, expected)

    def test_perform_operation_multiply(self):
        calc = MatrixCalculator()
        mat1 = calc.add_matrix([[1, 2], [3, 4]])
        mat2 = calc.add_matrix([[2, 0], [1, 2]])
        result = calc.perform_operation("multiply", 0, 1)
        expected = np.array([[4, 4], [10, 8]])
        np.testing.assert_array_equal(result.current_matrix, expected)

    def test_perform_operation_multiply_by_scalar(self):
        calc = MatrixCalculator()
        mat = calc.add_matrix([[1, 2], [3, 4]])
        scalar = 3
        result = calc.perform_operation("multiply_by_scalar", 0, scalar)
        expected = np.array([[3, 6], [9, 12]])
        np.testing.assert_array_equal(result.current_matrix, expected)

    def test_perform_operation_transpose(self):
        calc = MatrixCalculator()
        mat = calc.add_matrix([[1, 2, 3], [4, 5, 6]])
        result = calc.perform_operation("transpose", 0)
        expected = np.array([[1, 4], [2, 5], [3, 6]])
        np.testing.assert_array_equal(result.current_matrix, expected)

    def test_perform_operation_determinant(self):
        calc = MatrixCalculator()
        mat = calc.add_matrix([[4, 7], [2, 6]])
        result = calc.perform_operation("determinant", 0)
        self.assertAlmostEqual(result, 10.0)

    def test_perform_operation_unsupported(self):
        calc = MatrixCalculator()
        mat = calc.add_matrix([[1, 2], [3, 4]])
        with self.assertRaises(ValueError):
            calc.perform_operation("unsupported", 0)


if __name__ == '__main__':
    unittest.main()
