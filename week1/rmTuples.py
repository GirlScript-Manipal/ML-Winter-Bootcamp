seq=[(55),('hello'),(1,33),(),(),("hi","hey")]
filtered_seq=filter(lambda x : x!=(),seq)
print(list(filtered_seq))
seq.reverse()
filtered_rev=filter(lambda x: x!=(),seq)
print(list(filtered_rev))
