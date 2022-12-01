"""

This scripts solve problem number 2 level2.

the aim added to questiion.
"""

import re
aim = 0
horizantal = 0
depth = 0

with open("advent_of_code_l2.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
file.close()

for line in lines:
    if line.startswith('d'):
        temp = int(re.search(r'\d+', line).group())
        aim += temp
        print(f'aim is {aim} ,horizantal is {horizantal},depth is {depth}')
    if line.startswith('u'):
        temp = int(re.search(r'\d+', line).group())
        aim -= temp
        print(f'aim is {aim}, horizantal is {horizantal}, depth is {depth}')
    if line.startswith("f"):
        temp = int(re.search(r'\d+', line).group())
        if aim == 0:
            horizantal += temp
            print(f'aim is {aim} ,horizantal is {horizantal},depth is {depth}')
        else:
            horizantal += temp
            depth_change = temp * aim
            depth += depth_change
            print(f'aim is {aim} ,horizantal is {horizantal},depth is {depth}')
print(depth * horizantal)
