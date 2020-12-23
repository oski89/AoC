# Input data and make it a list of integers #
data = open("day-5-input")
my_list = list(map(int, list(data)))

#
# Part 1
#

# Initiate variables #
my_list1 = list(my_list)
step_count = 0
position = 0
jump_size = 0

# While inside the list, continue jumping #
while position < len(my_list1):
    jump_size = int(my_list1[position])
    my_list1[position] += 1
    position += jump_size
    step_count += 1

print("Answer to Part 1 is:", step_count)

#
# Part 2
#

# Reset variables #
my_list2 = list(my_list)
step_count = 0
position = 0
jump_size = 0

# While inside the list, continue jumping #
while position < len(my_list2):
    jump_size = int(my_list2[position])

    if jump_size >= 3:
        my_list2[position] -= 1
    else:
        my_list2[position] += 1

    position += jump_size
    step_count += 1

# Print the output #
print("Answer to Part 2 is:", step_count)