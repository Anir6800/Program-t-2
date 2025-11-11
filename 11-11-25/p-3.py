# 5.3 remove element from set

# 5.3.1
s = {1,2,3,4,5,6}
s.remove(4)
s.remove(5)
s.remove(6)
print(s)

# 5.3.2 discard element from set

a = {10,20,30,40,50}
a.discard(20)
print(a)

#DIFFERENCE BETWEEN REMOVE AND DISCARD
# IF ELEMENT IS NOT IN SET REMOVE WILL RAISE AN ERROR BUT DISCARD WONT RAISE ANY ERROR

# 5.3.3 clear the set
b = {100,200,300,400}
b.clear()
print(b)

# 5.3.4 delete the set
c = {7,8,9,10}
del c
#print(c) # this will raise an error as c is deleted

