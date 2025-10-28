# String Methods Demonstration
s = " hello world "

print(s.upper())        # Converts all characters to uppercase
print(s.lower())        # Converts all characters to lowercase
print(s.strip())        # Removes leading and trailing whitespace
print(s.replace("world", "there"))  # Replaces substring
print(s.split())        # Splits string into list of words
print(s.find("world"))  # Returns index where 'world' starts
print(s.startswith(" hello"))  # Checks if string starts with given substring
print(s.endswith("world "))    # Checks if string ends with given substring
print(s.count("l"))     # Counts occurrences of a character
print(s.capitalize())   # Capitalizes the first character
print(s.title())        # Capitalizes the first letter of each word
print(s.center(20, '*'))  # Centers string with '*' padding
print(s.isalpha())      # Checks if all characters are alphabetic
print(s.isdigit())      # Checks if all characters are digits
print(s.isspace())      # Checks if string contains only whitespace
print(s.join(["Hi", "There"]))  # Joins list elements using the string as separator
print(s.encode())       # Encodes string to bytes
print(s.zfill(20))      # Pads string with zeros to make it 20 characters long
print(s.partition("world"))   # Splits string into a tuple of 3 parts
print(s.swapcase())     # Swaps case of each character
print(s.translate(str.maketrans("hel", "123")))  # Character mapping
print(s.rstrip())       # Removes trailing whitespace
print(s.lstrip())       # Removes leading whitespace
print(s.removeprefix(" "))  # Removes specified prefix
print(s.removesuffix(" "))  # Removes specified suffix
print(s.rfind("o"))     # Finds last occurrence of substring
print(s.islower())      # Checks if all characters are lowercase
print(s.isupper())      # Checks if all characters are uppercase
print(s.istitle())      # Checks if string is titlecased
print(s.isnumeric())    # Checks if all characters are numeric
print(s.isdecimal())    # Checks if all characters are decimal digits
print(s.isidentifier()) # Checks if string is a valid identifier
print(s.casefold())     # Converts to lowercase (more aggressive)
print(s.index("world"))  # Returns index where 'world' starts (raises error if not found)

