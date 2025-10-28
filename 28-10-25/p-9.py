#Enumerate function
s = "hello"
for index, char in enumerate(s):
    print(f"Index: {index}, Character: {char}")
for index, char in enumerate(s, start=1):
    print(f"Index: {index}, Character: {char}")