from itertools import cycle

with open('input/01.txt', 'r') as file:
    my_data = file.read().split()

# Part 1
nums = list(map(int, my_data))
print('Part 1:', sum(nums))

# Part 2
seen = set([0])
ssum = 0
cnums = cycle(nums)

while True:
    ssum += next(cnums)
    if ssum in seen:
        break
    seen.add(ssum)

print('Part 2:', ssum)
