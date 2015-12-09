import re

__author__ = 'caleb'

lights = [[0 for y in range(1000)] for x in range(1000)]

with open('a.txt') as f:
    lines = f.readlines()

for line in lines:
    match = re.search(r"(turn on|toggle|turn off) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})", line)
    if match:
        x1 = int(match.group(2))
        x2 = int(match.group(4))
        y1 = int(match.group(3))
        y2 = int(match.group(5))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if match.group(1) == "turn on":
                    lights[x][y] += 1
                if match.group(1) == "turn off":
                    lights[x][y] -= 1
                    if lights[x][y] < 0:
                        lights[x][y] = 0
                if match.group(1) == "toggle":
                    lights[x][y] += 2

count = 0
for x in range(1000):
    for y in range(1000):
        count += lights[x][y]

print "I have " + str(count) + " brightness"
