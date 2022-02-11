
def remove(tuple):
    if tuple != 0:
        return tuple

list1 = [("x","y"),(2,5),("son","dad","mom"),(),(5,6,9,10),(),(2.34)]  

print(f"The original list: {list1}")
filtered = list(filter(remove,list1))
print(f"The filtered list: {filtered}")
filtered.reverse()
print(f"Result after reversing the filtered list: {filtered} ")


