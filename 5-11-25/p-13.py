numbers = [5, 3, 4, 100, -1, -2, 2]
numbers.sort()  # sort in place, preserves duplicates

if not numbers:
    max_length = 0
else:
    max_length = 1
    current_length = 1
    prev = numbers[0]

    for x in numbers[1:]:
        if x == prev:          # skip duplicates
            continue
        if x == prev + 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
        prev = x

print("Sorted List:", numbers)
print("Length of Longest Consecutive Sequence:", max_length)
