# tuple inbuilt functions
a = (5, 10, 15, 20, 25, 10, 30)
a.count(10)  # Count occurrences of 10
print("Count of 10 in Tuple:", a.count(10))
a.index(20)  # Find index of first occurrence of 20
print("Index of 20 in Tuple:", a.index(20))
print("Type of a:", type(a))
#starting index and ending index
print("Index of 10 in Tuple from index 2 to 6:", a.index(10, 2, 6))
print("Type of a:", type(a))
# Note: If the value is not found, index() will raise a ValueError.