# Key are immutable and values are mutable
my_dict = {
    (1, 2): [10, 20, 30],
    (3, 4): [40, 50, 60]
}
print("Dictionary with Tuple Keys:", my_dict)
type_of_my_dict = type(my_dict)
print("Type of my_dict:", type_of_my_dict)
