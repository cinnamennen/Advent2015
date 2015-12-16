import re

__author__ = 'caleb'

with open('a.txt') as f:
    lines = f.readlines()

sues = {}
read_sue = {"children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1}
for line in lines:
    s = re.search(r"Sue (\d*): (\w*): (\d*), (\w*): (\d*), (\w*): (\d*)", line)
    sues[s.group(1)] = {s.group(2): int(s.group(3)), s.group(4): int(s.group(5)), s.group(6): int(s.group(7))}
    # print "Sue " + str(s.group(1))
    for key, val in sues[s.group(1)].iteritems():
        # print "k: " + str(key) + ' v: ' + str(val)
        if key == 'cats' or key == 'trees':
            if val <= read_sue[key]:
                del sues[s.group(1)]
                break
        elif key == 'pomeranians' or key == 'goldfish':
            if val >= read_sue[key]:
                del sues[s.group(1)]
                break
        elif read_sue[key] != val:
            del sues[s.group(1)]
            break

print sues
