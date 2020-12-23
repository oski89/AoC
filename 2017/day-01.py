# Obtain input and store in list
with open('input/01.txt', 'r') as file:
    my_data = file.read()

# Part 1 #
sum1 = 0
for i, n in enumerate(my_data):
    if int(n) == int(my_data[i - 1]):
        sum1 += int(n)

print("Answer to part 1: ", sum1)

# Part 2 #
half = len(my_data) // 2
sum2 = 0
for i, n in enumerate(my_data):
    if int(n) == int(my_data[i - half]):
        sum2 += int(n)

print("Answer to part 2: ", sum2)
