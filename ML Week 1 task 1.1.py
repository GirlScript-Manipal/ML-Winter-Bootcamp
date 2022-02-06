
list1= [(5, 'Spaghetti'),(44, 'Penne'), (33,'Anelli'),(),(45, 'Cavatappi'), (), (53,'Maccheroni'),(),(69,'Bucatini')]
def funkshan(variable):
    if variable!=0:
        return variable
print("The original list:")
print(list1, "\n\n")
print("The filtered list:")
list2= list(filter(funkshan,list1))
print(list2,"\n\n")
print("The filtered and reversed list:")
list2.reverse()
print(list2)
#print('\n'.join(map(str, list2)))