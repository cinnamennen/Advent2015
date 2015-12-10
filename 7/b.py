import re

__author__ = 'caleb'

known = True
hidden = False
discovered = {}
undiscovered = {}
status = {}
a = None


class Wire:
    def __init__(self, my_name, gate, input_1, input_2=None, two_inputs=False):
        self.name = my_name  # string
        self.gate = gate  # string
        self.input_1 = input_1  # string
        self.input_2 = input_2  # string
        self.value = None  # integer
        self.two_inputs = two_inputs  # boolean


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


with open('b.txt') as f:
    lines = f.readlines()

for line in lines:
    simple = re.search(r"^(\w*) -> (\w*)", line)  # input_1 -> name
    invert = re.search(r"^NOT (\w*) -> (\w*)", line)  # NOT input_1 -> name
    catch = re.search(r"^(\w*) (\w*) (\w*) -> (\w*)", line)  # input_1 GATE input_2 -> name
    if simple:
        if is_number(simple.group(1)):
            my_type = 'HARD'
        else:
            my_type = 'REF'
        item = Wire(simple.group(2), my_type, simple.group(1))
        undiscovered[item.name] = item
        status[item.name] = hidden
    elif invert:
        item = Wire(invert.group(2), 'NOT', invert.group(1))
        undiscovered[item.name] = item
        status[item.name] = hidden
    elif catch:
        item = Wire(catch.group(4), catch.group(2), catch.group(1), catch.group(3))
        undiscovered[item.name] = item
        status[item.name] = hidden


def reveal(my_wire):
    status[my_wire.name] = known
    discovered[my_wire.name] = my_wire
    del undiscovered[my_wire.name]


def learn():
    global item, a
    while len(undiscovered) > 0:
        reveal_list = []
        for item in undiscovered:
            wire = undiscovered[item]
            if wire.gate == 'HARD':
                wire.value = int(wire.input_1)
                reveal_list.append(wire)
            elif wire.gate == 'REF':
                if status[wire.input_1] == known:
                    wire.value = int(discovered[wire.input_1].value)
                    reveal_list.append(wire)
            elif wire.gate == 'LSHIFT':
                if status[wire.input_1] == known and (is_number(wire.input_2) or status[wire.input_2] == known):
                    if is_number(wire.input_2):
                        shift = int(wire.input_2)
                    elif status[wire.input_2] == known:
                        shift = int(discovered[wire.input_2].value)
                    bits = int(discovered[wire.input_1].value)
                    wire.value = int(bits << shift)
                    reveal_list.append(wire)
            elif wire.gate == 'RSHIFT':
                if status[wire.input_1] == known and (is_number(wire.input_2) or status[wire.input_2] == known):
                    if is_number(wire.input_2):
                        shift = int(wire.input_2)
                    elif status[wire.input_2] == known:
                        shift = int(discovered[wire.input_2].value)
                    bits = int(discovered[wire.input_1].value)
                    wire.value = int(bits >> shift)
                    reveal_list.append(wire)
            elif wire.gate == 'NOT':
                if status[wire.input_1] == known:
                    wire.value = ~int(discovered[wire.input_1].value)
                    reveal_list.append(wire)
            elif wire.gate == 'AND':
                if (is_number(wire.input_1) or status[wire.input_1] == known) and (
                            is_number(wire.input_2) or status[wire.input_2] == known):
                    a = 0
                    b = 0
                    if is_number(wire.input_1):
                        a = int(wire.input_1)
                    elif status[wire.input_1] == known:
                        a = int(discovered[wire.input_1].value)
                    if is_number(wire.input_2):
                        b = int(wire.input_2)
                    elif status[wire.input_2] == known:
                        b = int(discovered[wire.input_2].value)
                    wire.value = int(a & b)
                    reveal_list.append(wire)
            elif wire.gate == 'OR':
                if (is_number(wire.input_1) or status[wire.input_1] == known) and (
                            is_number(wire.input_2) or status[wire.input_2] == known):
                    a = 0
                    b = 0
                    if is_number(wire.input_1):
                        a = int(wire.input_1)
                    elif status[wire.input_1] == known:
                        a = int(discovered[wire.input_1].value)
                    if is_number(wire.input_2):
                        b = int(wire.input_2)
                    elif status[wire.input_2] == known:
                        b = int(discovered[wire.input_2].value)
                    wire.value = int(a | b)
                    reveal_list.append(wire)
            else:
                print "Unknown type: " + str(wire.gate)
        for name in reveal_list:
            reveal(name)


learn()

a = discovered['a'].value
print "a is " + str(discovered['a'].value)


def reset():
    pass

#
# reset()
# learn()
# print "a is " + str(discovered['a'].value)
