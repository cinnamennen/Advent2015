__author__ = 'caleb'

x = 0
y = 0

houses = {'0:0': 1}

with open('a.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            print "End of file"
            break
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '<':
            x -= 1
        elif c == '>':
            x += 1
        else:
            print "Unknown character " + c
        loc = str(x) + ':' + str(y)
        # houses[loc] += 1
        if loc not in houses:
            houses[loc] = 1
        else:
            houses[loc] += 1


print "We visit " + str(len(houses)) + " houses"
