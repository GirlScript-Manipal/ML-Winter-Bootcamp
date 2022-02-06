#Code to remove empty tuples 
#Function using filter()
def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples
  
#Main code
tuples = [('Student1','16','10'),(), ('student2','15'), (), ('', ''), ('student3', '5'), ()]
print (Remove(tuples))