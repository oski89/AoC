# Generates the next number and returns it
def gen_num(num, val, div):
    return num * val % div


def main():
    # Default values
    val_a = 16807
    val_b = 48271
    div = 2147483647

    # Initial values for part 1
    num_a_1 = 703
    num_b_1 = 516
    iterations_1 = 40000000
    score_1 = 0

    for _ in range(0, iterations_1):
        num_a_1 = gen_num(num_a_1, val_a, div)
        num_b_1 = gen_num(num_b_1, val_b, div)

        if (num_a_1 & 0xFFFF) == (num_b_1 & 0xFFFF):
            score_1 += 1

    print('Answer to Part 1:', score_1)

    # Initial values for part 2
    num_a_2 = 703
    num_b_2 = 516
    iterations_2 = 5000000
    score_2 = 0

    for _ in range(0, iterations_2):
        while True:
            num_a_2 = gen_num(num_a_2, val_a, div)
            if num_a_2 % 4 == 0:
                break
        while True:
            num_b_2 = gen_num(num_b_2, val_b, div)
            if num_b_2 % 8 == 0:
                break

        if (num_a_2 & 0xFFFF) == (num_b_2 & 0xFFFF):
            score_2 += 1

    print('Answer to Part 2:', score_2)


if __name__ == '__main__':
    main()
