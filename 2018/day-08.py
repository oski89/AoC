with open('input/08.txt', 'r') as file:
    my_data = list(map(int, file.read().split()))

my_list = list(my_data)
meta_value = 0


def meta(total_list, ind):
    '''
    Takes a list, removes items based in index+1 and lowers children by 1.
    Returns the value of metadata and the new list.
    '''
    temp_ind = total_list[ind + 1]
    new_list = total_list[:ind] + total_list[ind + temp_ind + 2:]

    meta_value = sum(total_list[ind + 2:ind + temp_ind + 2])

    try:
        new_list[ind - 2] -= 1
    except:
        pass

    return meta_value, new_list


while my_list:
    for i, num in enumerate(my_list):
        if num == 0:
            m_value, my_list = meta(my_list, i)
            meta_value += m_value
            break

print("Part 1:", meta_value)


# Part 2

# A,  i, metadata
# 0, 11, 1, 4, 1, 7, 10, 4, 10, 6, 3, 7, 2

