with open('day-9-input') as f:
    INPUT = f.read()


# Function that deletes "!" and the character after
def ignore(in_tuple):
    in_string = in_tuple[0]
    start = in_string.find('!')
    end = in_string.find('!') + 2
    in_string = in_string[:start] + in_string[end:]
    return in_string, in_tuple[1]


# Function that deletes garbage (characters inside "<>") and returns the number of removed characters
def garbage(in_tuple):
    in_string = in_tuple[0]
    removed = 0
    start = in_string.find('<')
    end = in_string.find('>')
    if start != -1 and end != -1:
        removed = (len(in_string[start:end - 1]))
        in_string = in_string[:start] + in_string[end + 1:]
    return in_string, in_tuple[1] + removed


# Function that calculates the score of the groups
def group_score(in_string):
    value = 0
    score = 0
    new_string = in_string.replace(',', '')
    for c in new_string:
        if c == '{':
            value += 1
            score += value
        else:
            value -= 1
    return score


def main():
    my_tuple = (INPUT, 0)
    removed = 0

    while '!' in my_tuple[0]:
        my_tuple = ignore(my_tuple)

    while '<' in my_tuple[0]:
        my_tuple = garbage(my_tuple)

    score = group_score(my_tuple[0])
    removed = my_tuple[1]

    print("Answer to Part 1:", score)
    print("Answer to Part 2:", removed)


if __name__ == '__main__':
    main()
