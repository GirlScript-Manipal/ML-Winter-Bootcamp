
def Remove(tuples):
	tuples = list(filter(None, tuples))
	return tuples

tuples = [(), ('10','15','8'), (), ('a', 'b'),
		('100', 'ab', '45'), ('','')]
print(Remove(tuples))
