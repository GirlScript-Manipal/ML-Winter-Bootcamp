def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
tuples = [(), ('ryan','15','8'), (), ('a', 'suzanne'), 
          ('k', '56'),()]
print(Remove(tuples))


#using reverse()function
x =[(), ('ryan','15','8'), (), ('a', 'suzanne'), 
          ('k', '56'),()]
result = reversed(x)
result = tuple(result)
print(result)


#using filter()function
def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples
tuples = [(), ('ryan','15','8'), (), ('a', 'suzanne'), 
          ('k', '56'),()]
print (Remove(tuples))

#finding transpose of matrix using nested list
x = [[12,7],
    [4 ,5],
    [3 ,8]]
print(x)
result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
print("\n")
for r in result:
   print(r)

#finding transpose using 
import numpy as np
matrix=[[1,2,3],[4,5,6]]
print(matrix)
print("\n")
print(np.transpose(matrix))
