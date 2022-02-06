# Transpose of a matrix using Nested List Comprehensions
matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
for row in matrix:
    print(row)
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("\n")
for row in transpose:
    print(row)


# Transpose of a matrix using Numpy

import numpy as np
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(matrix)
print("\n")
print("Transpose: ")
print(np.transpose(matrix))
