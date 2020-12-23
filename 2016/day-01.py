# Obtain input and store in list #
file = open("input/01.txt", "r")
data = file.read()
my_list = data.split(", ")

#
# Part 1 #
#

test_list = ["R8", "R4", "R4", "R8"]

NESW = [0, 0, 0, 0]
index = 0
visited = [[0, 0, 0, 0]]

for action in my_list:
    direction = action[0]
    step_length = int(action[1:])

    if direction == "L":
        index -= 1
    else:
        index += 1

    index %= len(NESW)

    for i in range(0, step_length):
        NESW[index] += 1
        visited.append(list(NESW))

blocks1 = abs(NESW[0] - NESW[2]) + abs(NESW[1] - NESW[3])
print("Answer to part 1: ", blocks1)

#for places in visited:


file.close()
