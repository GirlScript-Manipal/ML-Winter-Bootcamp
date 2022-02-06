#Transpose
import numpy as np

m = [[1,2,3],[4,5,6]]
print("Original Matrix")
for row in m:
    print(row)
print("\nTranspose using Nest List Comprehension:")
t = [[m[j][i] for j in range(len(m))]for i in range(len(m[0]))]
for row in t:
    print(row)
print("\nTranspose using Numpy:")
mx = np.matrix('1,2,3;4,5,6')
nt = mx.transpose()
print(nt)
