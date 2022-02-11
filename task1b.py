import numpy as nm
a = nm.array([[123,345,456], [444,555,666]])
print ('input matrix:')
print(a)
b=nm.transpose(a)
print('transpose matrix:')
print(b)

a=[[123,345,456] , [444,555,666]]
print('input matrix:')
for x in a :
    print(x)

    b=[[a[j][i] for j in range (len(a))] for i in range (len(a[0]))]
    print('transpose matrix:')
    for y in b:
        print(y)
