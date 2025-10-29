def swap_case(s):
    result = ''
    for char in s:
        if char.isupper():
            result += chr(ord(char) + 32)
        elif char.islower():
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

string = "Hello World!"
swapped = swap_case(string)

print("Original String:", string)
print("Swapped Case String:", swapped)