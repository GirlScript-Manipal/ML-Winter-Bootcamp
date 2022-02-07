#Remove all empty tuples from a list. Perform this task using both reverse() function and filter() function.
from typing import Tuple



list_lang = [() , ('java'), ('swift'), () , ('python')]

def removetuple(list_lang):
    list_lang = filter(None , list_lang)
    return list_lang

print(removetuple(list_lang))

#Find the Transpose of a matrix using Nested List Comprehensions and Numpy.
m1 = [[1,2,3],[4,5,6]]
for row in m1:
    print(row)
    
transpose =[[m1[j][i] for j in range(len(m1)) ] for i in range(len(m1[0])) ]
print('\n')
for row in transpose:
    print(row)
    
    
#using numpy
import numpy as np
m1 = np.array([[1,2,3],[4,5,6]])
print(m1)
print('\n')
print('transpose:',m1.T)#Remove all empty tuples from a list. Perform this task using both reverse() function and filter() function.
from typing import Tuple



