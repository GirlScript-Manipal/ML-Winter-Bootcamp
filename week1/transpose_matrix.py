import numpy as np
m = [[9,8,7],[6,5,4]]
print("Matrix")
for row in m:
    print(row)
print("\nTranspose using Nested List Comprehension:")
tm = [[m[j][i] for j in range(len(m))]for i in range(len(m[0]))]
for row in tm:
    print(row)
print("\nTranspose using Numpy:")
matrix = np.matrix('9,8,7;6,5,4')
nt = matrix.transpose()
print(nt)