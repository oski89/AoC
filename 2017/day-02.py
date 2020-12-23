import numpy as np

with open('day-02-input', 'r') as file:
    my_data = [row.split() for row in file.readlines()]

my_data = [list(map(int, row)) for row in my_data]

sum1 = 0
for row in my_data:
    sum1 += max(row) - min(row)

print("Answer to part 1: ", sum1)

# Part 2 #

sum2 = 0

# Loop rows, find diviser and add to sum2
for row in my_data:
    row.sort(reverse=True)
    for num in row:
        for j in range(0, len(row)):
            if num % row[j] == 0 and num != row[j]:
                sum2 += int(num / row[j])

print("Answer to part 2: ", sum2)
