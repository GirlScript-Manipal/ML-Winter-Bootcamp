my_list = [(4,3), (), (2,4,5),()]

def my_func(item):
    if item != 0:
        return item


print(my_list)
new_list = list(filter(my_func, my_list))

print(new_list)
new_list.reverse()
print(new_list)

