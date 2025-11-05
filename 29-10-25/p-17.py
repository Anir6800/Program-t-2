# WAP to swap case of the string using isupper() and islower()
def swap_case(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result

string = "Hello World!"
swapped = swap_case(string)

print("Original String:", string)
print("Swapped Case String:", swapped)