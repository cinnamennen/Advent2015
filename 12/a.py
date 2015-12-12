import re

__author__ = 'caleb'

nums = []
with open('a.json') as f:
    lines = f.readlines()

for line in lines:
    nums += re.findall(r"(-?\d+)", line)

for x in range(len(nums)):
    nums[x] = int(nums[x])

print sum(nums)