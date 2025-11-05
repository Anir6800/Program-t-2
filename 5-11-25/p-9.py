#WAP to excract positive even numbers from a list and store them in another list.   
original_list = [-10, 15, 22, -33, 40, 55, -60, 72, 85, -90]
even_positive_list = []
for num in original_list:
    if num > 0 and num % 2 == 0:
        even_positive_list.append(num)
print("Original List:", original_list)
print("Even Positive Numbers List:", even_positive_list)

#one liner
even_positive_list_one_liner = [num for num in original_list if num > 0 and num % 2 == 0]
print("Even Positive Numbers List (One Liner):", even_positive_list_one_liner)