import re

__author__ = 'caleb'

s = '1321131112'


def gen_next(string):
    n = ""
    d = [m.group(0) for m in re.finditer(r"(\d)\1*", string)]
    for i in d:
        n += str(len(i)) + str(i[0])
    return n


for i in range(50):
    s = gen_next(s)

print len(s)