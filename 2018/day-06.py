import numpy as np

with open('day-06-input', 'r') as file:
    my_data = [tuple(map(int, row.strip('\n').split(', '))) for row in file.readlines()]

points = np.loadtxt('day-06-input', delimiter=', ')
xmin, ymin = points.min(axis=0) - 1
xmax, ymax = points.max(axis=0) + 2

#print(np.meshgrid(np.arange(xmin, xmax), np.arange(ymin, ymax)))
print(np.meshgrid(range(1, 3), range(2, 8)))


# xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(ymin, ymax))
