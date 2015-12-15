import re
import operator

__author__ = 'caleb'

with open('b.txt') as f:
    lines = f.readlines()

speeds = {}
distances = []
for line in lines:
    search = re.search(r"(\w*) can fly (\d*) km\/s for (\d*) seconds, but then must rest for (\d*) seconds\.", line)
    speeds[search.group(1)] = {'speed': int(search.group(2)), 'duration': int(search.group(3)), 'rest': int(
        search.group(4))}

for name, deer in speeds.iteritems():
    time_remaining = 2503
    must_rest = False
    distance = 0
    while time_remaining > 0:
        if must_rest is True:
            distance += 0
            must_rest = False
            time_remaining -= deer['rest']
        else:
            if deer['duration'] > time_remaining:
                fly_time = time_remaining
            else:
                fly_time = deer['duration']
            time_remaining -= fly_time
            distance += deer['speed'] * fly_time
            must_rest = True
    print name + ' has flown ' + str(distance)
    distances.append(distance)

print max(distances)
