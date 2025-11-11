#Set Comprehension
squares = {x**2 for x in range(10)}
print(squares)

#if
# Example of set comprehension with a condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)