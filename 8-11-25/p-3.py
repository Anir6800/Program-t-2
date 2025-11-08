#Accessing dictionary elements using keys
my_dict = {
    "fruit": "Apple",
    "quantity": 5,
    "price": 0.99
}
fruit = my_dict["fruit"]
quantity = my_dict["quantity"]
print("Fruit:", fruit)
print("Quantity:", quantity)

#for loop to iterate through dictionary keys
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")
    