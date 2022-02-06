L = [(), ('r','15','8'), (), ('n', 'r'), ('k', 'a', '45'), ('',''),()]
fL = filter(None, L)
print(list(fL))
L.reverse()
EmptyL = filter(None, L)
print(list(EmptyL))