import re


def nice(name):
    vowels = ('a', 'e', 'i', 'o', 'u')
    bad = ("ab", "cd", "pq", "xy")
    if not re.findall(r"(\w\w)[\w]*\1", name):
        return False
    elif not re.findall(r"(\w)\w\1", name):
        return False
    else:
        return True


with open('a.txt') as f:
    lines = f.readlines()

good = 0
for line in lines:
    if nice(line):
        good += 1

print str(good) + " good names"
