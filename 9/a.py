import re
from tsp_solver.greedy import solve_tsp

__author__ = 'caleb'

paths = []
initNode = None
cities = []
rename = {}
lookup = {}


class Path:
    def __init__(self, node_1, node_2, distance):
        self.distance = distance
        self.node_2 = node_2
        self.node_1 = node_1

    def dump(self):
        return "Node_1: " + str(self.node_1) + " Node_2: " + str(self.node_2) + " Dist: " + str(self.distance)


with open('b.txt') as f:
    lines = f.readlines()

for line in lines:
    search = re.search(r"(\w*) to (\w*) = (\d*)", line)
    if search:
        paths.append(Path(search.group(1), search.group(2), search.group(3)))
        if initNode is None:
            initNode = Path(search.group(1), search.group(2), search.group(3))
        if search.group(1) not in cities:
            cities.append(search.group(1))
        if search.group(2) not in cities:
            cities.append(search.group(2))

track = 0
for x in cities:
    rename[x] = track
    lookup[track] = x
    track += 1

elements = [[100000 for y in range(track)] for x in range(track)]
# print elements

for x in range(track):
    elements[x][x] = 0

for path in paths:
    coord_1 = rename[path.node_1]
    coord_2 = rename[path.node_2]
    elements[coord_1][coord_2] = int(path.distance)
    elements[coord_2][coord_1] = int(path.distance)

solution = solve_tsp(elements)
# print solution

print lookup
readable = []
for x in solution:
    # print lookup[x]
    readable.append(lookup[(x)])
    # pass
print readable


for i in range(len(readable)):
    print