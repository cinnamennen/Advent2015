import re


def nice(name):
    vowels = ('a', 'e', 'i', 'o', 'u')
    bad = ("ab", "cd", "pq", "xy")
    if (name.count(vowels[0]) + name.count(vowels[1]) + name.count(vowels[2]) + name.count(vowels[3]) + name.count(
            vowels[4])) < 3:
        return False
    elif not re.findall(r"(\w)\1", name):
        return False
    elif any(x in name for x in bad):
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
