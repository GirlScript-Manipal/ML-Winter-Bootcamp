import numpy
#tranpose using nested list comprehension
m=[[1,2,3],[4,5,6],[7,8,9]]
print("the transpose of the matrix")
for rows in m:
    print(rows)
print("\n")
columns=len(m[0])
row=len(m)
a=[]
b=[]
for i in range (row):
    for j in range (columns):
        a.append(m[j][i])
row1=[a[0],a[1],a[2]]
row2=[a[3],a[4],a[5]]
row3=[a[6],a[7],a[8]]
b.append(row1)
b.append(row2)
b.append(row3)
print("is")
print("\n")
for rows in b:
    print(rows)
print("\n")

#using numpy
m=numpy.matrix('[1,2,3;4,5,6;7,8,9]')
print("transpose of \n",m,"is")
matrix=m.transpose()
print("\n")
print(matrix)
