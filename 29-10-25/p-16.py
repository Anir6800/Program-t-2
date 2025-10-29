# WAP to create a function name length to  find length of string without len function 
def length(s):
    count = 0
    for char in s:
        count += 1
    return count

string = "Python"
print("String:", string)
print("Length of string:", length(string))