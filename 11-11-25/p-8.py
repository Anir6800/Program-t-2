# Wap to print sorted list of square of numbers using lambda function
#input = [-4,-5 ,6,3,2]
#output= [4,9,16,25,36]

input_list = [-4, -5, 6, 3, 2]
print(sorted(list(map(lambda x: x ** 2, input_list))))