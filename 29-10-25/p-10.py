# Itreation and enumerate in tuple
a = (100, 200, 300, 400, 500)
for item in a:
    print("Item:", item)
print("Type of a:", type(a))
for index, value in enumerate(a):
    print(f"Index: {index}, Value: {value}")