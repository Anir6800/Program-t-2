# WAP to count the frequency of each character in a string without using count function
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
string = "Anshi , Aniruddh , Mitanshi"
print("String:", string)
print("Character Frequency:", char_frequency(string))
