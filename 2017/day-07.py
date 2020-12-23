import re
from typing import NamedTuple, List, Set

TEST_INPUT = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


class Tower(NamedTuple):
    name: str
    weight: int
    children: List[str]


def process_line(line: str):
    parts = line.split(" -> ")
    tower = parts[0]
    children = [] if len(parts) == 1 else parts[1].split(", ")

    pattern = r'([a-z]+) \(([0-9]+)\)'
    match = re.match(pattern, tower)
    parent, weight = match.groups()
    weight = int(weight)

    return Tower(parent, weight, children)


assert process_line('fwft (72) -> ktlj, cntj, xhth') == Tower('fwft', 72, ['ktlj', 'cntj', 'xhth'])
assert process_line('havc (66)') == Tower('havc', 66, [])


def find_bottom(towers: List[Tower]) -> str:
    are_children: Set[str] = set()
    have_children: Set[str] = set()

    for tower in towers:
        if tower.children:
            have_children.add(tower.name)
        for child in tower.children:
            are_children.add(child)

    # Want the tower that has children but is not a child
    bottom_tower = [tower for tower in have_children if tower not in are_children]
    assert len(bottom_tower) == 1
    return bottom_tower[0]


TEST_TOWERS = [process_line(line) for line in TEST_INPUT.split("\n")]
assert find_bottom(TEST_TOWERS) == 'tknk'


def balance_towers(towers: List[Tower]):
    lookups = {tower.name: tower for tower in towers}

    def check(tower: Tower):
        """
        Return the total weight and is_balanced
        """
        subchecks = {name: check(lookups[name]) for name in tower.children}
        subcheck_weights = {weight for weight, _ in subchecks.values()}
        is_balanced = len(subcheck_weights) <= 1
        weight = tower.weight + sum(weight for weight, _ in subchecks.values())

        if len(subcheck_weights) > 1 and all(is_balanced for _, is_balanced in subchecks.values()):
            for name, (total_weight, is_balanced) in subchecks.items():
                children_tower = lookups[name]
                print(name, total_weight, children_tower.weight)

        return weight, is_balanced
    root = lookups[find_bottom(towers)]
    check(root)


if __name__ == '__main__':
    with open('day-7-input', 'r') as f:
        towers = [process_line(line.strip()) for line in f]
    print("Answer to Part 1:",find_bottom(towers))
    balance_towers(towers)
