with open('day-18-input') as f:
    INPUT = [lines.split() for lines in f.readlines()]

f2 = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

TEST_INPUT = [lines.split() for lines in f2.split('\n')]

# ---

registers = {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}
sent = {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}
ind = 0

# ---

while True:

    row = INPUT[ind]
    func = row[0]
    reg = row[1]
    try:
        num = int(row[2])
    except ValueError:
        num = registers[row[2]]
    except IndexError:
        num = None

    if func == 'set':
        registers[reg] = num
    elif func == 'add':
        registers[reg] += num
    elif func == 'mul':
        registers[reg] *= num
    elif func == 'mod':
        registers[reg] %= num
    elif func == 'snd':
        sent[reg] = registers[reg]
    elif func == 'rcv' and registers[reg] != 0:
        print('Answer to Part 1:', max(sent.values()))
        break
    elif func == 'jgz' and registers[reg] > 0:
        ind += num - 1
    ind += 1

