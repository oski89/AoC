my_number = [1, 1, 1, 3, 2, 2, 2, 1, 1, 3]


# Function that takes a number, plays look-and-say n times and returns final number
def look_and_say(number, times):
    all_numbers = []
    all_numbers.append(number)

    for _ in range(times):

        next_num = []
        counter = 0
        test_num = number[0]

        for idx, num in enumerate(number):
            if num == test_num:
                counter += 1
            else:
                next_num.append(counter)
                next_num.append(test_num)
                counter = 1
                test_num = int(num)

        next_num.append(counter)
        next_num.append(test_num)
        all_numbers.append(next_num)
        number = list(next_num)

    return next_num


if __name__ == '__main__':
    print(len(look_and_say(my_number, 50)))