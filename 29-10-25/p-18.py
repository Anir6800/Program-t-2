# WAP to extract usernamme from the email address
def extract_username(email):
    username = ''
    for char in email:
        if char == '@':
            break
        username += char
    return username
email = "anir6800@gmail.com"
print("Email Address:", email)
print("Username:", extract_username(email))

#Using split function
def extract_username_split(email):
    return email.split('@')[0]
email = "anir6800@gmail.com"
print("Email Address:", email)
print("Username using split:", extract_username_split(email))

#using index function
def extract_username_index(email):
    at_index = email.index('@')
    return email[:at_index]

email = "anir6800@gmail.com"
print("Email Address:", email)
print("Username using index:", extract_username_index(email))