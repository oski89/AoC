import re

with open('input/12.txt', 'r') as file:
    my_data = file.read()

numbers = re.findall(r'(-?\d+)', my_data)
print('Part 1:', sum([int(num) for num in numbers]))
