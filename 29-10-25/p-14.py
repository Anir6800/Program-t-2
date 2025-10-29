#Generator in tuples
t = (1,2,3,4,5,6)
g =  tuple(x*x for x in t)
for i in g:
    print(i)
print(g)