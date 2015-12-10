import re

__author__ = 'caleb'

with open('a.txt') as f:
    lines = f.readlines()
tot_size = 0
for line in lines:
    tot_size = tot_size - (len(line) - 1) + len(re.escape(line))
    # print "Add " + str(len(line)-1)
    # print "Sub " + str(len(ast.literal_eval(line)))
    # print "Line: " + line
    # print "Eval: " + ast.literal_eval(line)

print "Answer is " + str(tot_size+1)
