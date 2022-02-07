import numpy as num

a = num.array([[111,222,333] , [444,555,666]])
print("Input Matrix:")
print(a)
b = num.transpose(a)
print("Transpose  Matrix: ")
print(b)

a = [[111,222,333] , [444,555,666]]
print("Input Matrix:")
for x in a:
    print(x)

b = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
print("\n Transpose Matrix: ")
for y in b:
    print(y)
