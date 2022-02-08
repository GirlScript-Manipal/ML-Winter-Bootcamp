# Remove empty tuples from a list
def removetuple(num):
    num = filter(None, num)
    return num

num = [(), (1, 2), (3, 4), (), (5, 6), ()]
print("List:")
print(list(num))
print("Filtered list in reverse:")
num.reverse()
print(list(removetuple(num)))

