#Compression Operator
s = "hello world"
s1 = "Hello World"
s2 = "hello world"
print(s == s2)      # True
print(s == s1)      # False
print(ord('a'))     # 97
print(ord('A'))     # 65
print(s<s1)       # False (because lowercase 'h' has a higher ASCII value than uppercase 'H'
print(s1<s)       # True