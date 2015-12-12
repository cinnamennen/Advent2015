import json
import re
import yaml

__author__ = 'caleb'

nums = []

with open('a.json') as f:
    j = yaml.safe_load(f)


def assess(item):
    if type(item) is int:
        return item
    elif type(item) is list:
        return sum([assess(x) for x in item])
    elif type(item) is not dict:
        return 0
    elif type(item) is dict and 'red' in item.values():
        return 0
    else:
        capture = [item.values()]
        # noinspection PyTypeChecker
        return assess(capture)


print assess(j)
