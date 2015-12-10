__author__ = 'caleb'

sqft = 0
with open('a.txt') as f:
    lines = f.readlines()

for line in lines:
    (l, w, h) = line.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    a, b, c = (l * w, l * h, w * h)
    area = 2 * a + 2 * b + 2 * c + min(a, b, c)
    sqft += area

print "Need " + str(sqft)
