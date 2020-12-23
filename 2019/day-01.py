from math import floor

with open('input/01.txt', 'r') as file:
    my_data = file.read().split()

# Part 1
sum1 = 0
for num in my_data:
    sum1 += floor(float(num)/3) - 2

print(f'Part 1: {sum1}')

# Part 2
sum2 = 0
for num in my_data:
    fuel_done = False
    while not fuel_done:
        fuel = floor(float(num)/3) - 2
        if fuel > 0:
            sum2 += fuel
            num = fuel
        else:
            fuel_done = True

print(f'Part 2: {sum2}')
