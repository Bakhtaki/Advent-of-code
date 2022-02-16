"""
This is part One of level2.

In this level base on file advant_of_cdoe_l2.txt
we will calculate the distance.
"""
import re


Horizantal = 0
Vertical = 0
with open("advent_of_code_l2.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
file.close()
lines = [line.rstrip() for line in lines]
for line in lines:
    if line.startswith("f"):
        temp = int(re.search(r'\d+', line).group())
        Horizantal += temp
    if line.startswith("d"):
        temp = int(re.search(r" \d+", line).group())
        Vertical += temp
    if line.startswith("u"):
        temp = int(re.search(r"\d+", line).group())
        Vertical -= temp
print(Horizantal * Vertical)
