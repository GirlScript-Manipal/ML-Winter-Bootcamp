def emptytuples(List):
    List=filter(None,List)
    return List

List=[( ),("Harry"),("Stark"),( ),("David"),( ),("oscar"),("parker")]
List.reverse()
print(list(emptytuples(List)))

