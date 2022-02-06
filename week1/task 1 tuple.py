# to remove all the empty tuples from a list
tup = [(), ("kevin", "john", "pety"), (1, 2, 3), ("hello", "bye"), (), (55, 77), (), ("python")]
tup.reverse()
filtered_list1 = filter(lambda x: x != (), tup)
print(list(filtered_list1))

