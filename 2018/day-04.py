import re
from collections import defaultdict
import numpy

with open('input/04.txt', 'r') as file:
    my_data = sorted(file.readlines())

my_dict = defaultdict()
pattern = r"^.*(\d{2}).*(\d{2}).*(\d{2}).*(\d{2})\]\s(?:Guard #)?(\w+).*$"

for row in my_data:
    month, day, hour, minute, ID = re.match(pattern, row).groups()
    try:
        guard = int(ID)
        if guard not in my_dict.keys():
            my_dict[guard] = 0
    except:
        if ID == 'falls':
            sleep = 0
            falls = int(minute)
        elif ID == 'wakes':
            sleep = int(minute) - falls
            my_dict[guard] += sleep

# Finds the sleepiest guard and the total amount of mins that guard is asleep
max_k, max_v = 0, 0
for k, v in my_dict.items():
    if v > max_v:
        max_k, max_v = k, v

# Determine how many times the sleepiest guard is mentioned
counter = 0
for row in my_data:
    if '#' + str(max_k) in row:
        counter += 1

# Present the data in a grid; rows = each info, cols = minutes
grid = numpy.zeros((1,60), dtype=int)
correct_guard = False

for row in my_data:
    month, day, hour, minute, ID = re.match(pattern, row).groups()
    try:
        guard = int(ID)
        if guard == max_k:
            correct_guard = True
        else:
            correct_guard = False
    except:
        if correct_guard:
            if ID == 'falls':
                falls = int(minute)
            elif ID == 'wakes':
                wakes = int(minute)
                grid[0, falls:wakes] += 1

sleep_minute = grid.argmax()
print("Part 1:", max_k * sleep_minute)

# Part 2
g_dict = defaultdict()
coin = 0

# Create a dict with each unique guard index as 1, 2, 3, 4, etc
for row in my_data:
    month, day, hour, minute, ID = re.match(pattern, row).groups()
    try:
        guard = int(ID)
        if guard not in g_dict:
            g_dict[guard] = coin
            coin += 1
    except:
        pass

n_guards = len(g_dict)

# Present the data in a grid; rows = guard, cols = minutes
grid2 = numpy.zeros((n_guards,60), dtype=int)

for row in my_data:
    month, day, hour, minute, ID = re.match(pattern, row).groups()
    try:
        guard = int(ID)
    except:
        if ID == 'falls':
            falls = int(minute)
        elif ID == 'wakes':
            wakes = int(minute)
            grid2[g_dict[guard], falls:wakes] += 1

max2_minute = numpy.argmax(grid2) % 60

for k, v in g_dict.items():
    if v == 9:
        max2_guard = k

print("Part 2:", max2_minute * max2_guard)
