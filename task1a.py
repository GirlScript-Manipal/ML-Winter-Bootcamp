t= [() , (1,2,3) ,(), ('T','H','O','R') , ("MARVEL"), ()]
def main (variable):
  if variable!=0:
    return variable
print ("The original list:")
print(t)
m= list(filter(main, t))
print ("Result after removing all empty tuples")
m.reverse()
print (m)