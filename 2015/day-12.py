import re

with open('day-12-input', 'r') as file:
    my_data = file.read()

numbers = re.findall(r'(-?\d+)', my_data)
print 'Part 1:', sum([int(num) for num in numbers])
