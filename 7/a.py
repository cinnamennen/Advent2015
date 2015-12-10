import re

__author__ = 'caleb'

dependencies = {}
values = {}
gates = {}

class Wire:
    def __init__(self, name, type, input_1, input_2):
        self.name = name
        self.type = type
        self.input_1 = input_1
        self.input_2 = input_2
        self.value = None


def lookup(element):
    element = str(element)
    if dependencies.get(element) is None:
        if values.get(element) is None:
            print "I couldn't find " + str(element)
        else:
            return values.get(element)
    else:
        gate_type = gates.get(element)
        if gate_type is None:
            print "Couldn't get the gate for " + str(element)
        else:
            if gate_type == 'NOT':
                result = lookup(dependencies.get(element)[0])
                result = ~int(result)
                values[element] = result
                resolve(element)
            elif gate_type == 'IS':
                result = lookup(dependencies.get(element)[0])
                result = int(result)
                values[element] = result
                resolve(element)
            elif gate_type == 'LSHIFT':
                amount = int(dependencies[element][1])
                shift = int(lookup(dependencies[element][0]))
                result = shift << amount
                values[element] = result
                resolve(element)
            elif gate_type == 'RSHIFT':
                amount = int(dependencies[element][1])
                shift = int(lookup(dependencies[element][0]))
                result = shift >> amount
                values[element] = result
                resolve(element)
            elif gate_type == 'AND':
                first = int(lookup(dependencies[element][0]))
                second = int(lookup(dependencies[element][1]))
                result = first & second
                values[element] = result
                resolve(element)
            elif gate_type == 'OR':
                first = int(lookup(dependencies[element][0]))
                second = int(lookup(dependencies[element][1]))
                result = first | second
                values[element] = result
                resolve(element)
            return values.get(element)


def resolve(element):
    # del dependencies[element]
    # if gates.get(element) is not None:
    #     del gates[element]
    pass


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


with open('a.txt') as f:
    lines = f.readlines()

for line in lines:
    simple = re.search(r"^(\d*) -> (\s*)", line)
    invert = re.search(r"^NOT (\w*) -> (\w*)", line)
    catch = re.search(r"^(\w*) (\w*) (\w*) -> (\w*)", line)
    if simple:
        if is_number(simple.group(1)):
            values[simple.group(2)] = int(simple.group(1))
        else:
            dependencies[simple.group(2)] = [simple.group(2)]
            gates[simple.group(2)] = 'IS'
    elif invert:
        dependencies[invert.group(2)] = [invert.group(1)]
        gates[invert.group(2)] = 'NOT'
    elif catch:
        dependencies[catch.group(4)] = [catch.group(1), catch.group(3)]
        gates[catch.group(4)] = catch.group(2)




# print "The value of a is " + str(lookup('lx'))
if dependencies.get('a') is None:
    print values.get('a')
print values

# print values
