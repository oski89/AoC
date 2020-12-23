from __future__ import print_function

with open('input/05.txt', 'r') as file:
    my_data = file.read()

def rem_pol(string):
    init_len = len(string)
    for c in set(string):
        string = string.replace(c.upper() + c.lower(), '').replace(c.lower() + c.upper(), '')
    return init_len != len(string), string

my_data1 = str(my_data)

while True:
    changed, my_data1 = rem_pol(my_data1)
    if not changed:
        break

print("Part 1:", len(my_data1))

counter = len(my_data1)

for c in 'abcdefghijklmnopqrstuvwxyz':
    my_data2 = str(my_data)
    my_data2 = my_data2.replace(c, '').replace(c.upper(), '')

    while True:
        changed, my_data2 = rem_pol(my_data2)
        if not changed:
            if len(my_data2) < counter:
                counter = len(my_data2)
            break

print("Part 2:", counter)
