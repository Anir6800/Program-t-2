# wap to print even numbers from a tuple using continue statement
s = (6,7,8,4,2,5,9,1,3,0)
for i in range(len(s)):
    if s[i] % 2 == 0:
        print(s[i])
    else:
        continue
