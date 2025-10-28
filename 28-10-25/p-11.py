# WAP to count number of spaces, uppercase, lowercase, and digits in a string
S = "This is a Python 101 Course"

spaces = 0
uppercase = 0
lowercase = 0
digits = 0

for char in S:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

print("Spaces:", spaces)
print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Digits:", digits)
