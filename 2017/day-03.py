import numpy as np
import math

number = 368078  # sqrt = 606.694321714

test_number = 23
tn = int(math.ceil(math.sqrt(test_number)))

grid = np.zeros((tn, tn), int)

ix, iy = tn // 2, tn // 2
xinc, yinc = 1, 1

n = 1
for _ in range(8):
    for y in range(yinc):
        for x in range(xinc):
            grid[ix + x][iy + y] = n
            n += 1
        xinc += 1
        xinc *= -1
    yinc += 1
    yinc *= -1


print(grid)
