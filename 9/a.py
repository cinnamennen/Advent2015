import re

__author__ = 'caleb'

paths = []
initNode = None
cities = []
assigned = []


class Path:
    def __init__(self, node_1, node_2, distance):
        self.distance = distance
        self.node_2 = node_2
        self.node_1 = node_1

    def dump(self):
        return "Node_1: " + str(self.node_1) + " Node_2: " + str(self.node_2) + " Dist: " + str(self.distance)


def get_all_containing(name, usable_paths):
    rv = []
    for x in usable_paths:
        if x.node_1 == name or x.node_2 == name:
            rv.append(x)
    return x


def generate_path(free_cities, available_paths, attached_cities, built_path):
    if not free_cities:
        total = 0
        for items in built_path:
            total += int(items.distance)
            print "    Path: " + items.dump()
        print "Base case: " + str(total)
        return total

    my_min = []

    for options in available_paths:
        print "looking at " + options.dump()
        if options.node_1 not in attached_cities and options.node_2 not in attached_cities:
            print "Impossible"
            continue
        else:
            if options.node_1 in free_cities:
                pivot = options.node_1
                root = options.node_2
            else:
                pivot = options.node_2
                root = options.node_1
            print "adding " + options.dump()
            free_cities.remove(pivot)
            available_paths.remove(options)
            attached_cities.append(pivot)
            built_path.append(options)
            my_min.append(generate_path(free_cities, available_paths,
                                        attached_cities, built_path))
            free_cities.append(pivot)
            available_paths.append(options)
            attached_cities.remove(pivot)
            built_path.remove(options)

    return min(my_min)

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

cities.remove(initNode.node_1)
assigned.append(initNode.node_1)
print "Init is " + str(initNode.node_1)
print generate_path(cities, paths, assigned, [])

