import math
import numpy as np

with open("day01/input.txt", "r") as inp:
    data = [x.strip() for x in inp.readlines()]
    
digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
res_1, res_2 = 0, 0
for line in data:
    lowest, highest = [-1 for _ in range(10)], [-1 for _ in range(10)]
    found_first = False
    for c in line:
        if c.isnumeric() and not found_first:
            found_first = True
            first, last = c, c
        elif c.isnumeric():
            last = c
    res_1 += int(first + last)
    for k, v in digits.items():
        a = np.array([line.find(k), line.find(str(v))])
        if len(a[a >= 0]) > 0:
            lowest[v] = a[a >= 0].min()
        highest[v] = max(line.rfind(k), line.rfind(str(v)))
    high = highest.index(max(highest))
    curr = math.inf
    low = high
    for i, x in enumerate(lowest):
        if x != -1 and x < curr:
            curr = x
            low = i
    res_2 += int(str(low) + str(high))
            
print(f"Part 1: {res_1}")
print(f"Part 2: {res_2}")