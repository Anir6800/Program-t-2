#5.6  Lambda function and annonymous function 
#  it's  an online function 
#  it's dosent have return value and return function name
#  it's nameless function with multiple arguments returing on valid expression 
square = lambda x: x ** 2
print(square(5))
add = lambda a, b: a + b
print(add(10, 20))

# Example of using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Example of using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Example of using lambda with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)