import numpy
#List Comprehension Method
M = [[1,2,3], [4,5,6], [7,8,9]]
MT = []
for i in range(3):
    MT.append([row[i] for row in M])
MT = [[row[i] for row in M] for i in range(3)]
for j in MT :
    print (j)

#Numpy Method
m=numpy.matrix('[1,2,3;4,5,6;7,8,9]')
print("transpose of \n",m,"is")
matrix=m.transpose()
print("\n")
print(matrix)