import ast

__author__ = 'caleb'

with open('a.txt') as f:
    lines = f.readlines()
tot_size = 1
for line in lines:
    tot_size += len(line) - len(ast.literal_eval(line)) - 1
    # print "Add " + str(len(line)-1)
    # print "Sub " + str(len(ast.literal_eval(line)))
    # print "Line: " + line
    # print "Eval: " + ast.literal_eval(line)

print "Answer is " + str(tot_size)
