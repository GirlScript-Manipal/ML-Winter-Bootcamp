# Remove empty tuples from a list
def remove_tuples(a):
    a = filter(None, a)
    return a
a =[ (), ('math'), (), ('english'), (), ('science'), ('social') ]
a.reverse()
print(a)
print(remove_tuples(a))

# Transposing a matrix using numpy
import numpy as np
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print (matrix)
print(np.transpose(matrix))

# Transposing a matrix using nested list comprehensions
m = [[1,2,3],[4,5,6],[7,8,9]]
for row in m:
    print(row)
transposed_m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
for row in transposed_m:
    print(row)