#LIST methods

#1. append()
my_list = [10, 20, 30]
print("Original List:", my_list)
#Appending an element
my_list.append(40)
print("List after append:", my_list)
#appending a tuple
my_list.append((50, 60))
print("List after appending a tuple:", my_list)

#2. extend()
my_list = [10, 20, 30]
print("Original List:", my_list)
#Extending the list with another list
my_list.extend([40, 50])
print("List after extend:", my_list)

#3.clear() and del()
my_list = [10, 20, 30]
print("Original List:", my_list)
#Clearing the list
my_list.clear()
print("List after clear:", my_list)
#Deleting the list
del my_list
#deleting the element at index 0
my_list = [10, 20, 30]  
print("Original List:", my_list)
del my_list[0]
print("List after deleting index 0:", my_list)

#4. Copy()
my_list = [10, 20, 30]
print("Original List:", my_list)
#Copying the list
copied_list = my_list.copy()
print("Copied List:", copied_list)
#copying an element
element_copy = my_list[1:3].copy()
print("Element Copy:", element_copy)
#referring the same list
ref_list = my_list
print("Reference List:", ref_list)
#modifying original list
my_list[0] = 100
print("Modified Original List:", my_list)
print("Reference List after modification:", ref_list)

#5. count()
my_list = [10, 20, 30, 20, 40, 20]
print("Original List:", my_list)
#Counting occurrences of 20
count_20 = my_list.count(20)
print("Count of 20 in the list:", count_20)
#Counting occurrences of 50
count_50 = my_list.count(50)
print("Count of 50 in the list:", count_50)

#6. index()
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)
#Finding index of element 30
index_30 = my_list.index(30)
print("Index of 30 in the list:", index_30)
#Finding index of element 10
index_10 = my_list.index(10)
print("Index of 10 in the list:", index_10)

#7. insert()
my_list = [10, 20, 30]
print("Original List:", my_list)
#Inserting 15 at index 1
my_list.insert(1, 15)
print("List after insert:", my_list)
#inserting 5 at index -1
my_list.insert(-1, 5)
print("List after inserting 5 at index -1:", my_list)

#8. pop()
my_list = [10, 20, 30, 40]
print("Original List:", my_list)
#Popping the last element
popped_element = my_list.pop()
print("Popped Element:", popped_element)
print("List after pop:", my_list)
#Popping element at index 1
popped_index_1 = my_list.pop(1)
print("Popped Element at index 1:", popped_index_1)
print("List after popping index 1:", my_list)

#9. remove()
my_list = [10, 20, 30, 20, 40]
print("Original List:", my_list)
#Removing first occurrence of 20
my_list.remove(20)
print("List after remove:", my_list)
#Removing element 10
my_list.remove(10)
print("List after removing 10:", my_list)

#10. reverse()
my_list = [10, 20, 30, 40]
print("Original List:", my_list)
#Reversing the list
my_list.reverse()
print("Reversed List:", my_list)

#11. sort()
my_list = [30, 10, 40, 20]
print("Original List:", my_list)
#Sorting the list
my_list.sort()
print("Sorted List:", my_list)
#Sorting in descending order
my_list.sort(reverse=True)
print("Sorted List in Descending Order:", my_list)

