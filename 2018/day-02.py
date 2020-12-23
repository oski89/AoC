from collections import Counter

with open('input/02.txt', 'r') as file:
    my_data = file.read().split()

# Part 1
twos = 0
threes = 0

for row in my_data:
    d_data = Counter(row)
    if 2 in d_data.values():
        twos += 1
    if 3 in d_data.values():
        threes += 1

print("Part 1:", twos * threes)

# Part 2
counter = 0

for i, test_row in enumerate(my_data):
    for comp_row in my_data[i + 1:]:
        for a, b in zip(test_row, comp_row):
            if a != b:
                counter += 1
        else:
            if counter == 1:
                string = ''
                for c, d in zip(test_row, comp_row):
                    if c == d:
                        string += c
                print("Part 2:", string)
        counter = 0
