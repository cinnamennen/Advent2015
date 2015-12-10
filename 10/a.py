import re

s = '1321131112'


def gen_next(string):
    n = ""
    d = [m.group(0) for m in re.finditer(r"(\d)\1*", string)]
    for j in d:
        n += str(len(j)) + str(j[0])
    return n


for i in range(40):
    s = gen_next(s)

print len(s)
