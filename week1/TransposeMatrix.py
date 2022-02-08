# Transpose of a matrix
import numpy as np

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Matrix:\n")
print(matrix)

print("\nTranspose of Matrix using nested list comprehension:\n")
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for row in transpose:
    print(row)

print("\nTranspose of Matrix using numpy:\n")
print(np.transpose(matrix))
