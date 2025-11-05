# WAP TO FIND SUM OF ELEMENTS IN A LIST EXCPET 13 WHICH IS UNLUCKY NUMBER ALSO DONT COUNT THE NUNMBER IMMEDIATELY AFTER 13
INPUT =  [1,2,4,13,100,5,6]
total = 0
skip_next = False
for num in INPUT:
    if skip_next:
        skip_next = False
        continue
    if num == 13:
        skip_next = True
        continue
    total += num
print("Sum of elements except 13 and the number after it is:", total)

#Method 2
INPUT =  [1,2,4,13,100,5,6]
total = 0
i = 0
while i < len(INPUT):
    if INPUT[i] == 13:
        i += 2  # Skip 13 and the next number
        continue
    total += INPUT[i]
    i += 1
print("Sum of elements except 13 and the number after it is:", total)

#method 3
INPUT =  [1,2,4,13,100,5,6]
total = 0
for i in range(len(INPUT)):
    if INPUT[i] == 13:
        continue
    if i > 0 and INPUT[i-1] == 13:
        continue
    total += INPUT[i]
print("Sum of elements except 13 and the number after it is:", total)
