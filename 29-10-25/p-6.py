#indexing and Slicing of tuple
a = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print("Original Tuple:", a)
print("Element at index 2:", a[2])          # Accessing element at index 2
print("Elements from index 2 to 5:", a[2:6]) # Slicing from index 2 to 5
print("Elements from start to index 4:", a[:5]) # Slicing from start to index 4
print("Elements from index 5 to end:", a[5:]) # Slicing from index 5 to end
print("Last element:", a[-1])                # Accessing last element
print("Elements from index -5 to -2:", a[-5:-1]) # Slicing using negative indices
print("Reversed Tuple:", a[::-1])           # Reversing the tuple
print("Every second element:", a[::2])      # Slicing with step