__author__ = 'caleb'

santa = [0, 0]
robo = [0, 0]

turn = 0

team = [santa, robo]

houses = {'0:0': 1}

with open('a.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            print "End of file"
            break
        if c == '^':
            team[turn][1] += 1
        elif c == 'v':
            team[turn][1] -= 1
        elif c == '<':
            team[turn][0] -= 1
        elif c == '>':
            team[turn][0] += 1
        else:
            print "Unknown character " + c
        loc = str(team[turn][0]) + ':' + str(team[turn][1])
        # houses[loc] += 1
        if loc not in houses:
            houses[loc] = 1
        else:
            houses[loc] += 1
        turn += 1
        turn %= 2

print "We visit " + str(len(houses)) + " houses"
