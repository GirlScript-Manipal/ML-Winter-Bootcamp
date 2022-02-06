def emptytuples(a):
    new=filter(None,a)
    return new

list1=[('Taylor Swift'),('Selena Gomez'),(),('Aurora'),('Coldplay'),()]
print(list(emptytuples(list1)))