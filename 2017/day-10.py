from typing import List

with open('input/10.txt') as f:
    my_lengths: List[int] = [int(x) for x in f.read().split(',')]


def main():
    my_list: List[int] = list(range(0, 256))
    skip = 0
    pos = 0
    for length in my_lengths:
        temp_list = my_list[pos:] + my_list[:pos]
        temp_list = list(reversed(temp_list[:length])) + temp_list[length:]
        my_list = temp_list[-pos:] + temp_list[:-pos]
        pos += (length + skip)
        pos %= len(my_list)
        skip += 1

    print('Answer to Part 1:', my_list[0] * my_list[1])


if __name__ == '__main__':
    main()
