#WAP to find the sum of postivite and negative numbers using lambda function
numbers = [10, -5, 3, -1, 7, -2, 8, -4]
positive_sum = sum(filter(lambda x: x > 0, numbers))
negative_sum = sum(filter(lambda x: x < 0, numbers))
print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)