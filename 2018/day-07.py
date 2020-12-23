import string

with open('input/07.txt', 'r') as file:
    my_data = file.read().strip().split('\n')

rules = dict.fromkeys(string.ascii_uppercase, [])

for row in sorted(my_data):
    first, then = row[5], row[-12]
    if rules[then] == []:
        rules[then] = list(first)
    else:
        rules[then].append(first)

step_order = []
while rules:
    for k, v in rules.items():
        if not v:
            step_order.append(k)
            del rules[k]
            for kk, vv in rules.items():
                try:
                    if k in vv:
                        vv.remove(k)
                        rules[kk] == vv
                except TypeError:
                    pass
            else:
                break

print("Part 1:", ''.join(step_order))
