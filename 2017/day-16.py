from typing import List

TEST_INPUT = 's1,x3/4,pe/b'
with open('input/16.txt') as f:
    INPUT = f.read()


# Function that spins x programs from the end to the front
def spin(in_string: str, times: int) -> str:
    out_string = in_string[-times:] + in_string[:-times]
    return out_string


# Function that swaps programs at positions pos_1 and pos_2
def exchange(in_string: str, pos1: int, pos2: int) -> str:
    name1 = in_string[pos1]
    name2 = in_string[pos2]
    dummy = '!'
    out_string = in_string.replace(name2, dummy).replace(name1, name2).replace(dummy, name1)
    return out_string


# Function that swaps programs with names name_1 and name_2
def partner(in_string: str, name1: str, name2: str) -> str:
    dummy = '!'
    out_string = in_string.replace(name2, dummy).replace(name1, name2).replace(dummy, name1)
    return out_string


def main():
    # Starting order of the programs
    my_programs = "abcdefghijklmnop"

    # Split the input string into a list of strings separated by comma
    my_list: List[str] = INPUT.split(',')

    # Loop through the list for each element and call the appropriate function
    for action in my_list:
        if action[0] == 's':
            times = int(action[1:])
            my_programs = spin(my_programs, times)
        elif action[0] == 'x':
            list_pos = action.split('/')
            pos_1 = int(list_pos[0][1:])
            pos_2 = int(list_pos[1])
            my_programs = exchange(my_programs, pos_1, pos_2)
        else:
            name_1 = action[1]
            name_2 = action[3]
            my_programs = partner(my_programs, name_1, name_2)

    # Print the result
    print('Answer to Part 1:', my_programs)

    # Perform 1 billion dances/actions
    for _ in range(1, 100000):
        # Loop through the list for each element and call the appropriate function
        for action in my_list:
            if action[0] == 's':
                times = int(action[1:])
                my_programs = spin(my_programs, times)
            elif action[0] == 'x':
                list_pos = action.split('/')
                pos_1 = int(list_pos[0][1:])
                pos_2 = int(list_pos[1])
                my_programs = exchange(my_programs, pos_1, pos_2)
            else:
                name_1 = action[1]
                name_2 = action[3]
                my_programs = partner(my_programs, name_1, name_2)

    # Print the result
    print('Answer to Part 2:', my_programs)


if __name__ == '__main__':
    main()
