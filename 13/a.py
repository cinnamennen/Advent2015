import itertools
import re

__author__ = 'caleb'

names = []

rules = {}
max_joy = None
best_combo = None


def calculate(arrangement):
    return_value = 0
    for index in range(len(arrangement[:-1])):
        return_value += rules[arrangement[index]][arrangement[index+1]]
    return_value += rules[arrangement[-1]][arrangement[0]]
    for index in range(1,len(arrangement)):
        # print index
        return_value += rules[arrangement[index]][arrangement[index-1]]
    return_value += rules[arrangement[0]][arrangement[-1]]

    return return_value


with open('a.txt') as f:
    lines = f.readlines()

for line in lines:
    search = re.search(r"(\w*) would (gain|lose) (\d*) happiness units by sitting next to (\w*)\.", line)
    if search.group(2) == 'gain':
        units = int(search.group(3))
    else:
        units = -1 * int(search.group(3))
    if search.group(1) not in names:
        names.append(search.group(1))
    if search.group(4) not in names:
        names.append(search.group(4))
    if search.group(1) not in rules:
        rules[search.group(1)] = {}

    rules[search.group(1)][search.group(4)] = units

combinations = list(itertools.permutations(names, len(names)))
# print combinations

joy = []
for choice in combinations:
    joy.append(calculate(choice))
    # print joy[-1]
print max(joy)
