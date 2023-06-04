#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

# Valid test cases
print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))  # Expected output: [[7, 10], [15, 22]]
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))  # Expected output: [[13, 16]]

# Invalid test cases
# m_a and m_b are not lists
try:
    print(matrix_mul("invalid", [[1, 2], [3, 4]]))
except TypeError as e:
    print(e)  # Expected output: m_a must be a list or m_b must be a list

# m_a and m_b are not lists of lists
try:
    print(matrix_mul([[1, 2], [3, 4]], [1, 2]))
except TypeError as e:
    print(e)  # Expected output: m_a must be a list of lists or m_b must be a list of lists

# m_a is empty
try:
    print(matrix_mul([], [[1, 2], [3, 4]]))
except ValueError as e:
    print(e)  # Expected output: m_a can't be empty

# m_b is empty
try:
    print(matrix_mul([[1, 2], [3, 4]], []))
except ValueError as e:
    print(e)  # Expected output: m_b can't be empty

# m_a contains non-integer/float elements
try:
    print(matrix_mul([[1, 2], [3, "invalid"]], [[1, 2], [3, 4]]))
except TypeError as e:
    print(e)  # Expected output: m_a should contain only integers or floats

# m_b contains non-integer/float elements
try:
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, "invalid"]]))
except TypeError as e:
    print(e)  # Expected output: m_b should contain only integers or floats

# m_a rows are of different sizes
try:
    print(matrix_mul([[1, 2], [3], [4, 5]], [[1, 2], [3, 4]]))
except TypeError as e:
    print(e)  # Expected output: each row of m_a must be of the same size

# m_b rows are of different sizes
try:
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3], [4, 5]]))
except TypeError as e:
    print(e)  # Expected output: each row of m_b must be of the same size

# m_a and m_b can't be multiplied
try:
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]]))
except ValueError as e:
    print(e)  # Expected output: m_a and m_b can't be multiplied
