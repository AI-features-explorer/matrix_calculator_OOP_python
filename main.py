import os
from matrix_calculator import MatrixCalculator
from matrix import DimensionError, MultiplicationError, DeterminantError


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def parse_matrix():
    rows = int(input("Enter the number of rows: "))
    matrix = []
    for i in range(rows):
        row = list(map(float, input("Enter the row values separated by space: ").split()))
        matrix.append(row)
    return matrix


def print_matrices(calculator):
    if len(calculator.matrices) == 0:
        print("No matrices available.")
        return
    print("\nAvailable matrices:")
    for index, matrix in enumerate(calculator.matrices):
        print(f"Matrix {index}:")
        for row in matrix.matrix:
            print(", ".join(map(str, row)))
    print()


def main():
    calculator = MatrixCalculator()

    while True:
        clear_console()  # Clear the console at the start of the loop
        try:
            print_matrices(calculator)  # Display available matrices and their indices
            print("Matrix Calculator")
            print("1. Add Matrix")
            print("2. Perform Operation")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                matrix = parse_matrix()
                calculator.add_matrix(matrix)
                print("Matrix added.")
            elif choice == "2":
                operation = input("Enter operation (add, multiply, multiply_by_scalar, transpose, determinant): ")
                if operation in ["add", "multiply"]:
                    index1 = int(input("First matrix index: "))
                    index2 = int(input("Second matrix index: "))
                    result = calculator.perform_operation(operation, index1, index2)
                elif operation in ["multiply_by_scalar", "transpose", "determinant"]:
                    index = int(input("Matrix index: "))
                    if operation == "multiply_by_scalar":
                        scalar = float(input("Enter scalar value: "))
                        result = calculator.perform_operation(operation, index, scalar)
                    else:
                        result = calculator.perform_operation(operation, index)
                print("Result:")
                if operation == "determinant":
                    print(result)
                else:
                    for row in result.matrix:
                        print(" ".join(map(str, row)))
                input("Press enter to confirm the result...")  # User confirms the result
            elif choice == "3":
                break
            else:
                print("Invalid option. Please try again.")
        except DimensionError as e:
            print(f"Dimension Error: {e.message}")
        except MultiplicationError as e:
            print(f"Multiplication Error: {e.message}")
        except DeterminantError as e:
            print(f"Determinant Error: {e.message}")
        except ValueError:
            print("Invalid index or input. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Exiting program.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
