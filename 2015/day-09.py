with open('input/09.txt', 'r') as file:
    data = file.read().split('\n')

import re
routes = [re.compile(r'^(\w+)\s.*\s(\w+)\s.*\s(\d*)$').findall(row) for row in data]

dest_list = []

[dest_list.append(row[0][0]) for row in routes if row[0][0] not in dest_list]
[dest_list.append(row[0][1]) for row in routes if row[0][1] not in dest_list]

