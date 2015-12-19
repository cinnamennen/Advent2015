import re

__author__ = 'caleb'

combinations = set()
actions = {}
other = []
with open('replacements.txt') as f:
    lines = f.readlines()
with open('input.txt') as g:
    molecule = g.readlines()[0]

for q in range(len(lines)):
    search = re.search(r'(\w*) => (\w*)', lines[q])
    if search.group(1) in actions:
        actions[search.group(1)].append(search.group(2))
    else:
        actions[search.group(1)] = [search.group(2)]

# print actions
# print molecule

for key, val in actions.iteritems():
    # print 'key: {0}'.format(key)
    # print '  val: {0}'.format(val)
    l = [i for i in range(len(molecule)) if molecule.startswith(key, i)]
    # print l
    for rep in val:
        for index in l:
            # print molecule[:index] + '|' + molecule[index:index + len(key)] + '|' + molecule[index + 1:]
            # print molecule[:index] + '|' + molecule[index:index + len(key)].replace(key, rep) + '|' + molecule[index + 1:]
            combinations.add(
                molecule[0:index] + molecule[index:].replace(key, rep, 1))

print len(combinations)
# print len(other)
# print combinations
