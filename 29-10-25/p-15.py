# zip tuples
t1 = (1,2,3)
t2 = ('a','b','c')
z = zip(t1, t2)
for i in z:
    print(i)
print(tuple(zip(t1, t2)))
