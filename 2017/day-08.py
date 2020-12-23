from typing import List, Dict

with open('day-8-input') as f:
    INPUT = f.read().split("\n")


def check_condition(my_dict: Dict, cond: List[str]) -> bool:
    if cond[1] == '>':
        return my_dict[cond[0]] > int(cond[2])
    if cond[1] == '>=':
        return my_dict[cond[0]] >= int(cond[2])
    if cond[1] == '<':
        return my_dict[cond[0]] < int(cond[2])
    if cond[1] == '<=':
        return my_dict[cond[0]] <= int(cond[2])
    if cond[1] == '==':
        return my_dict[cond[0]] == int(cond[2])
    if cond[1] == '!=':
        return my_dict[cond[0]] != int(cond[2])


def main():
    # Identify all unique registers and store them in dictionary with zero as initial value #
    registers = []
    [registers.append(line.split(" ")[0]) for line in INPUT if not line.split(" ")[0] in registers]
    registers.sort()
    reg_dict = {k: 0 for k in registers}

    max_dict_value = 0

    # Loop through every row and perform the action if condition is met #
    for row in INPUT:
        row = row.split()
        active_register = row[0]
        inc_dec = row[1]
        number = int(row[2])
        cond_list = row[4:]

        # Evaluate condition and return True or False
        if not check_condition(reg_dict, cond_list):
            pass
        elif inc_dec == 'inc':
            reg_dict[active_register] += number
        else:
            reg_dict[active_register] -= number

        if max(reg_dict.values()) > max_dict_value:
            max_dict_value = max(reg_dict.values())

    print("Answer to Part 1:", max(reg_dict.values()))
    print("Answer to Part 2:", max_dict_value)


if __name__ == '__main__':
    main()
