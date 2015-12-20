from random import shuffle
import re

__author__ = 'caleb'

rules = []
version = ''

with open('replacements' + version + '.txt') as f:
    lines = f.readlines()
with open('input' + version + '.txt') as g:
    molecule = g.readlines()[0]

for q in range(len(lines)):
    search = re.search(r'(\w*) => (\w*)', lines[q])
    # if search.group(2) in actions:
    #     actions[search.group(2)].append(search.group(1))
    # else:
    rules.append((search.group(1), search.group(2)))

target = molecule
count = 0
print rules

while target != 'e':
    swap = target
    for a, b in rules:
        if b not in target:
            continue
        else:
            target = target.replace(b, a, 1)
            count += 1
    if swap == target:
        target = molecule
        part2 = 0
        shuffle(rules)

print count
