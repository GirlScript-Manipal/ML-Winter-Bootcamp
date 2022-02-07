#Transpose of a matrix using Nested List Comprehensions and Numpy
import numpy as np

Matrix = [[10,20,30],[40,50,60],[70,80,90]]
print("Original Matrix is : ")
for row in Matrix:
    print(row)
print("\nTranspose using Nest List Comprehension:")
Transpose = [[Matrix[j][i] for j in range(len(Matrix))]for i in range(len(Matrix[0]))]
for row in Transpose:
    print(row)
print("\nTranspose of Matrix using Numpy:")
matrix= np.matrix('10,20,30;40,50,60;70,80,90')
transpose = matrix.transpose()
print(transpose)