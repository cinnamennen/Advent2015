import re
import operator

__author__ = 'caleb'

with open('a.txt') as f:
    lines = f.readlines()


class Deer:
    def __init__(self, speed, flight_time, rest_time, name):
        self.name = name
        self.rest_time = int(rest_time)
        self.flight_time = int(flight_time)
        self.speed = int(speed)
        self.is_resting = False
        self.flight_remaining = self.flight_time
        self.rest_remaining = 0
        self.distance = 0
        self.points = 0

    def simulate(self):
        if self.is_resting:
            if self.rest_remaining == 0:
                self.is_resting = False
                self.flight_remaining = self.flight_time
                self.flight_remaining -= 1
                self.distance += self.speed
            else:
                self.rest_remaining -= 1
        else:
            if self.flight_remaining == 0:
                self.is_resting = True
                self.rest_remaining = self.rest_time
                self.rest_remaining -= 1
            else:
                self.flight_remaining -= 1
                self.distance += self.speed


deer = {}
for line in lines:
    search = re.search(r"(\w*) can fly (\d*) km\/s for (\d*) seconds, but then must rest for (\d*) seconds\.", line)
    deer_name = search.group(1)
    deer[deer_name] = Deer(search.group(2), search.group(3), search.group(4), search.group(1))

time = 2503
for i in range(time):
    max_dist = -10
    for value in deer.values():
        value.simulate()
    for value in deer.values():
        if value.distance > max_dist:
            max_dist = value.distance
    for value in deer.values():
        if value.distance == max_dist:
            value.points += 1

travel = []
for key, value in deer.iteritems():
    travel.append(value.points)
print max(travel)
# for val in deer.values():
#     print val.name + ": " + str(val.points)
