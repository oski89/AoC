import re

with open('input/12.txt', 'r') as file:
    my_data = file.read().split('\n')


# Part 1
gen = re.search(r"([\.#]+)", my_data[0]).group()


rules = {}
for row in my_data[2:]:
    k, v = row.split(' => ')
    rules[k] = v


def new_gen(curr_gen, rules):

    curr_gen = '....' + curr_gen + '....'
    next_gen = ''

    for i in range(2, len(curr_gen) - 2):
        next_gen += rules[curr_gen[i - 2:i + 3]]

    return next_gen


def sum_gen(curr_gen):

    diff = (len(curr_gen) - 100) // 2
    ssum = 0

    for i, c in enumerate(curr_gen):
        if c == '#':
            ssum += (i - diff)

    return ssum


for i in range(20):
    gen = new_gen(gen, rules)

print("Part 1:", sum_gen(gen))

# Part 2
# Pattern: 293 + 62 * n
print("Part 2:", 293 + 62 * 50000000000)
