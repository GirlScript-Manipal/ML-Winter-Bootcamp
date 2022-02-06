#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Find the Transpose of a matrix using Nested List Comprehensions and Numpy.
#transpose using numpy
import numpy as np

m = np.array([[111,222,333] , [444,555,666]])
print("original matrix:")
print(m)
t = np.transpose(m)
print("transpose: ")
print(t)


# In[22]:


#transpose using nested list comprehension
m = [[111,222,333] , [444,555,666]]
print("original matrix:")
for x in m:
    print(x)

t = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n transpose: ")
for y in t:
    print(y)

