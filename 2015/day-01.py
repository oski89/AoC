# Obtain input and store in list
with open('input/01.txt', 'r') as f:
    data = f.read()

x = 0
y = 0
my_list = []

for par in data:
    y += 1
    if par == '(':
        x += 1
    else:
        x -= 1
    if x == -1:
        my_list.append(y)

print('Answer to part 1:', x)

print('Answer to part 2:', my_list[0])
