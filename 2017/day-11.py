with open("input/11.txt", "r") as f:
    data = f.read().split(",")

x = 0
y = 0
dist = 0
dist_max = 0

for d in data:
    if d == 'ne':
        x += 1
    if d == 'n':
        x += 1
        y += 1
    if d == 'nw':
        y += 1
    if d == 'sw':
        x -= 1
    if d == 's':
        x -= 1
        y -= 1
    if d == 'se':
        y -= 1

    if x >= 0 and y >=0 or x < 0 and y < 0:
        dist = max(abs(x), abs(y))
    else:
        dist = abs(x) + abs(y)

    if dist > dist_max:
        dist_max = dist

print("Answer for Part 1:", dist)
print("Answer for Part 2:", dist_max)
