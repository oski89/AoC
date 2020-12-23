from typing import *

TEST_INPUT = "0	2	7	0"

with open('input/06.txt') as f:
    INPUT = f.read()


# Function that takes a bank, redistributes it and returns its new configuration
def reallocate(in_banks: List[int]) -> List[int]:
    out_banks: List[int] = in_banks
    num = max(in_banks)
    ind = in_banks.index(num)
    out_banks[ind] = 0
    for i in range(1, num + 1):
        out_banks[(ind + i) % len(in_banks)] += 1

    return out_banks


def main():
    banks: List[int] = [int(num) for num in INPUT.split("\t")]
    seen_banks: List[List[int]] = []
    counter: int = 0

    # Loop as long as there is no copy of banks in seen_banks
    while banks not in seen_banks:
        seen_banks.append(list(banks))
        banks = reallocate(banks)
        counter += 1

    print("Answer to Part 1:", counter)

    # Reset for part 2
    counter = 0
    seen_banks = []
    # Loop as long as there is no copy of banks in seen_banks
    while banks not in seen_banks:
        seen_banks.append(list(banks))
        banks = reallocate(banks)
        counter += 1

    print("Answer to Part 2:", counter)


if __name__ == '__main__':
    main()
