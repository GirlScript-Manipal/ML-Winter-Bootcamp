# Find the Transpose of a matrix using Nested List Comprehensions .
print("original matrix:")
matrix = [[1,5,7] ,[2,4,6]]
for i in matrix:
    print(i)

print("")

print("transpose matrix: " )
transpose = [[matrix[j][k] for j in range(len(matrix))] for k in range(len(matrix[0]))]
for l in transpose:
    print(l)





# Find the Transpose of a matrix using Numpy.
import numpy as np

matrix = np.array([[1,5,7] ,[2,4,6]])
print(f'''Input Matrix: 
{matrix}''')

transpose = np.transpose(matrix)
print(f'''Transpose  Matrix:
{transpose}''')


