with open('input/23.txt') as f:
    INPUT = [lines.split() for lines in f.readlines()]

# ---

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
ind = 0
count = 0

# ---

while ind < 11:

    row = INPUT[ind]
    func = row[0]
    reg = row[1]
    try:
        num = int(row[2])
    except ValueError:
        num = registers[row[2]]

    if func == 'set':
        registers[reg] = num
    elif func == 'sub':
        registers[reg] -= num
    elif func == 'mul':
        registers[reg] *= num
    elif func == 'jnz' and reg != 0:
        ind += num
    ind += 1

print('Answer to Part 1:', count)
print((registers['b'] - registers['e']) * (registers['b'] - registers['d']))