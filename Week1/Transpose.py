X = [[3,5,10],
    [1,2,4],
    [7,9,4]]

result = [[X[j][i]
for j in range(len(X))]
          for i in range(len(X[0]))]

for r in result:
    print(r)
    
    
#using numpy
    
import numpy as np

m = np.array([[3,5,10] , [1,2,4] , [7,9,4])
t = np.transpose(m)
print("Transpose matrix: ")
print(t)
