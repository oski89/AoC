import numpy as np
import re

with open('input/03.txt', 'r') as file:
    my_data = file.readlines()

# Part 1
grid = np.zeros((1000, 1000), int)

for row in my_data:
    ID, x, y, dx, dy = map(int, re.findall(r"[\d]+", row))
    grid[y:y + dy, x:x + dx] += 1

print("Part 1:", np.count_nonzero(grid >= 2))

# Part 2
grid = np.zeros((1000, 1000), int)

for row in my_data:
    ID, x, y, dx, dy = map(int, re.findall(r"[\d]+", row))
    grid[y:y + dy, x:x + dx] += ID

for row in my_data:
    ID, x, y, dx, dy = map(int, re.findall(r"[\d]+", row))
    if sum(sum(grid[y:y + dy, x:x + dx])) == ID * dx * dy:
        print("Part 2:", ID)
