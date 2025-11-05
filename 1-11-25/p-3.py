# password validation 1 capital letter, 1 small letter, 1 digit, 1 special character, min length 16 using loops

password = input("Enter your password: ")
if len(password) < 16:
    print("Password must be at least 16 characters long.")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    if has_upper and has_lower and has_digit and has_special:
        print("Password is valid.")
    else:
        print("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")