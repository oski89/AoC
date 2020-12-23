import numpy

gsn = 2694
square = 300

grid = numpy.zeros((square, square), dtype=int)

for x in range(square):
    for y in range(square):
        rid = x + 10
        pl = rid * y
        pl += gsn
        pl *= rid
        try:
            pl = int(str(pl)[-3])
        except IndexError:
            pl = 0
        pl -= 5
        grid[y, x] = pl

# Part 1
sum1 = 0
xtop = 0
ytop = 0
for x in range(square - 2):
    for y in range(square - 2):
        tsum = sum(sum(grid[y:y + 3, x:x + 3]))
        if tsum > sum1:
            sum1 = tsum
            xtop = x
            ytop = y

print(f"Part 1: {xtop},{ytop}")

# Part 2
sum2 = 0
xtop2 = 0
ytop2 = 0
for i in range(300):
    for x in range(square - i):
        for y in range(square - i):
            tsum = sum(sum(grid[y:y + (i + 1), x:x + (i + 1)]))
            if tsum > sum2:
                sum2 = tsum
                xtop2 = x
                ytop2 = y
                size = i + 1

print(f"Part 2: {xtop2},{ytop2},{size}")
