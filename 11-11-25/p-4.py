# set oprations 
# 5.4 set operations union, intersection, difference, symmetric difference

#5.4.1 union operation
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.union(s2)
print("Union of s1 and s2 is:", s3)

# second method - not in syllabus 
s4 = s1 | s2
print("Union of s1 and s2 using | operator is:", s4)

#5.4.2 intersection operation
s5 = s1.intersection(s2)    
print("Intersection of s1 and s2 is:", s5)

# second method - not in syllabus
s6 = s1 & s2
print("Intersection of s1 and s2 using & operator is:", s6)

#5.4.3 difference operation
s7 = s1.difference(s2)
print("Difference of s1 and s2 (s1 - s2) is:", s7)

s11 = s2.difference(s1)
print("Difference of s2 and s1 (s2 - s1) is:", s11)

# second method - not in syallbus 
s8 = s1 - s2
print("Difference of s1 and s2 (s1 - s2) using - operator is:", s8)
s12 = s2 - s1
print("Difference of s1 and s1 (s2 - s1) using - operator is:", s12)

#5.4.4 symmetric difference operation
s9 = s1.symmetric_difference(s2)
print("Symmetric Difference of s1 and s2 is:", s9)

# second method - not in syllabus
s10 = s1 ^ s2
print("Symmetric Difference of s1 and s2 using ^ operator is:", s10)


# 5.4.5 issubset , issuperset, isdisjoint

s1 = {1,2,3}
s2 = {0,1,2,3,4,5,6}
print("Subset, Superset and Disjoint operations")
print("s1:", s1)
print("s2:", s2)
print("Is s1 a subset of s2?:", s1.issubset(s2))
print("Is s2 a superset of s1?:", s2.issuperset(s1))
print("Are s1 and s2 disjoint sets?:", s1.isdisjoint(s2))
