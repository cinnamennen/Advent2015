from itertools import combinations

__author__ = 'caleb'

containers = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
containers2 = [20,15,10,5,5]
volume = 150
count = 0
min_count = {}

for i in range(len(containers)):
    for pick in list(combinations(containers, i)):
        if sum(pick) == volume:
            if len(pick) in min_count:
                min_count[len(pick)] += 1
            else:
                min_count[len(pick)] = 1
                # print pick
print min_count[min(min_count.keys())]
# print min_count
