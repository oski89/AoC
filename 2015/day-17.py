from itertools import combinations

with open('day-17-input', 'r') as file:
    my_number = file.read().split()

my_list = sorted([int(num) for num in my_number], reverse=True)
total_volume = 150
counter = 0
combos = []

for n in range(len(my_list)):
    for combo in combinations(my_list, n):
        if sum(combo) == 150:
            combos.append(combo)
            counter += 1

print 'Part 1:', counter

min_len = len(combos[0])
counter2 = 0

for tup in combos:
    if len(tup) == min_len:
        counter2 += 1

print 'Part 2:', counter2
