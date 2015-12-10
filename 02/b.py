__author__ = 'caleb'

sqft = 0
with open('a.txt') as f:
    lines = f.readlines()

for line in lines:
    (l, w, h) = line.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    sqft += 2 * l + 2 * h + 2 * w - 2 * max(l, w, h)
    sqft += l * w * h

print "Need " + str(sqft)
