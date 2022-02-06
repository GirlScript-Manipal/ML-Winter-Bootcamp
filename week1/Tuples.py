#Empty Tuples

L = [(),('A','B'),('c','d','e'),(),(24,25),()]
filtered_L = filter(None, L)
print("Filter()")
print(list(filtered_L))

L.reverse()
filtered_revL = filter(None, L)
print("Reverse() and Filter()")
print(list(filtered_revL))
