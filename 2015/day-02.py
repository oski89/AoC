# Obtain input and store in list #
dim = open('2_input')

total_paper = 0

total_ribbon = 0

for line in dim:
    lwh_list = line.split("x")
    lwh_list[2] = lwh_list[2].replace('\n', '')
    lwh_list = list(map(int, lwh_list))

    # Sort so that l < w < h
    lwh_list.sort()

    print(lwh_list)

    l = lwh_list[0]
    w = lwh_list[1]
    h = lwh_list[2]

    surf_area = 2*l*w + 2*w*h + 2*h*l
    small_area = l * w

    total_paper += surf_area + small_area

    ribbon_present = 2 * l + 2 * w
    ribbon_bow = l * w * h
    total_ribbon += ribbon_present + ribbon_bow

print("Answer to part 1:", total_paper)
print("Answer to part 2:", total_ribbon)

dim.close()