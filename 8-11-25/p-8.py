#other dicitionary methods
my_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

# clear() method to remove all items
my_dict.clear()
print("Dictionary after clear():", my_dict)

# copy() method to create a shallow copy
my_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict)

#reference vs copy
ref_dict = my_dict
ref_dict["A"] = 10
print("Original Dictionary after modifying reference:", my_dict)
print("Reference Dictionary:", ref_dict)
print("Copied Dictionary remains unchanged:", copied_dict)

# fromkeys() method to create a new dictionary with specified keys and a default value
keys = ['X', 'Y', 'Z']
new_dict = dict.fromkeys(keys, 0)
print("New Dictionary from fromkeys():", new_dict)

dict_items = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
d = dict.fromkeys(dict_items, "default_value")
print("Dictionary from fromkeys() with default value:", d)

#pop() method to remove and return an arbitrary item
my_dict = {
    "name": "Bob",
    "age": 28,
    "city": "Chicago"
}
print("Original Dictionary:", my_dict)
removed_item = my_dict.popitem()
print("Removed Item:", removed_item)
print("Dictionary after popitem():", my_dict)

#pop() method to remove a specified item
my_dict = {
    "name": "Bob",
    "age": 28,
    "city": "Chicago"
}
print("Original Dictionary:", my_dict)
removed_value = my_dict.pop("age")
print("Removed Value:", removed_value)
print("Dictionary after pop():", my_dict)

# setdefault() method to get a value and set a default if the key does not exist
my_dict = {     
    "name": "Bob",
    "age": 28,
    "city": "Chicago"
}
print("Original Dictionary:", my_dict)
age = my_dict.setdefault("age", 30)
print("Age:", age)
print("Dictionary after setdefault():", my_dict)

my_dict = {
    "name": "Bob",
    "age": 28,
    "city": "Chicago"
}
print("Original Dictionary:", my_dict)
country = my_dict.setdefault("country", "USA")
print("Country:", country)
print("Dictionary after setdefault() for new key:", my_dict)

# update() method to update dictionary with another dictionary's items
my_dict = {
    "name": "Bob",
    "age": 28,
    "city": "Chicago"
}
print("Original Dictionary:", my_dict)
new_info = {
    "age": 29,
    "country": "USA"
}
my_dict.update(new_info)
print("Dictionary after update():", my_dict)

