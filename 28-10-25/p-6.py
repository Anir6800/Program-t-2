#Logical Operators
s = "hello world"
s1 = "Hello World"
print(s or s1)     # 'hello world' (since s is non-empty, it is returned)
print(" " or s1)   # ' ' (space is non-empty, so it is returned)
print("" or s1)    # 'Hello World' (since the first string is empty, s1 is returned)
print(s and s1)    # 'Hello World' (since both are non-empty, the last operand is returned)
print("" and s1)   # '' (since the first string is empty, it is returned)
print(s and " ")   # ' ' (since both are non-empty, the last operand is returned)
print(not s)       # False (non-empty strings are considered True)
print(not "")      # True (empty string is considered False)