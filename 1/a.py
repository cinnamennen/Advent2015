__author__ = 'caleb'

f = open('a.txt', 'r')

floor = 0
while True:
    c = f.read(1)
    if not c:
        print "Floor " + str(floor)
        break
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    else:
        print "Undefined char: " + c

