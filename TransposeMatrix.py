import numpy as np
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("The given matrix is:\n")
print(matrix)
print("\n")

#Using Nested list Compensations
transpose=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("The transpose of the given matrix using Nested list comprehensions is:\n")
print(transpose)
print("\n")

#Using numpy
print("The transpose of the given matrix using numpy is:\n")
print(matrix.T)