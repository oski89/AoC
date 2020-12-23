with open('input/12.txt') as f:
    INPUT = f.read().split('\n')

# Create a dictionary with integers as keys and list of integers as values
my_dict = {}
for line in INPUT:
    i = (int(line.split(' <-> ')[0]))
    my_dict[i] = (list(map(int, line.split(' <-> ')[1].split(', '))))

# Initial values
group = [[]]
i = 0
start_id = 0
connecting = list(my_dict[start_id])

#while len(connecting) < len(my_dict):
for number in connecting:
    if number not in group[i]:
        group[i].append(number)
        [connecting.append(el) for el in my_dict[number] if el not in connecting]

i += 1

if start_id in connecting:
    start_id += 1

print('Answer to Part 1:', len(group[0]))
#print('Answer to Part 2:', len(group))