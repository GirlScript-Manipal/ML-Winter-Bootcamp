def remove(list):
    list=filter(None, list)
    return list
list=[ ('0', '1'), (), ('2', '3', '4'), (), ('5', '6') ]
print(remove(list))