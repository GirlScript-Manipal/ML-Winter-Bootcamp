#Removing empty tuples from a list using reverse() & filter() functions
List = [("a","b","c","d"),(),('S','I'),(),('D','d','H'),(),(1,2,3,4,5,6,25),()]
filteredList = filter(None, List)
print("Filtered list is : \n")
print(list(filteredList))

List.reverse()
reversedFilteredList = filter(None, List)
print("List After Reversing and Filtering is : \n")
print(list(reversedFilteredList))