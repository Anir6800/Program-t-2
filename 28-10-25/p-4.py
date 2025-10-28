#Universal Methods
#min,max,sorted
s = "hello world"
print(min(s))      # ' ' (space character has the lowest ASCII value)
print(max(s))      # 'w' (character with the highest ASCII value)   
print(sorted(s))   # [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(sorted(s,reverse=True))   # ['w', 'r', 'o', 'o', 'l', 'l', 'l', 'h', 'e', 'd', ' ']
