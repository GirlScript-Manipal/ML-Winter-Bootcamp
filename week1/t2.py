import numpy

matrix = [[5, 8, 10],
          [7, 9, 0],
          [1, 4, 69]]
Transpose = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
       Transpose[j][i] = matrix[i][j]

print(Transpose)

matrixTranspose = numpy.transpose(matrix)
print(matrixTranspose)
