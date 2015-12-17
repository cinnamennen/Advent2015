from itertools import combinations

__author__ = 'caleb'


containers = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
volume = 150
count = 0

for i in range(len(containers)):
    for pick in list(combinations(containers,i)):
        if sum(pick) == volume:
            count += 1
            # print pick
print count