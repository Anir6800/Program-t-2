#Maketrans and Translate Example
original = "Hello World"
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
translated = original.translate(trantab)
print(translated)  # H2ll4 W4rld
