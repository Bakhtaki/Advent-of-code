"""
This script related to advent of code 2021.

Level 3 Part 1
"""

gama_rate = ''
epsilon_rate = ''

with open('advent_of_code_l3.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
file.close()
loop = len(lines[0])  # length of each line
for i in range(loop):
    count_zero = 0
    count_one = 0
    for line in lines:
        check = line[i]
        if check == "1":
            count_one += 1
        if check == "0":
            count_zero += 1
    if count_one > count_zero:
        gama_rate += "1"
        epsilon_rate += "0"
    else:
        gama_rate += "0"
        epsilon_rate += "1"

gama_rate_decimal = int(gama_rate, 2)
epsilon_rate_decimal = int(epsilon_rate, 2)
print(gama_rate_decimal * epsilon_rate_decimal)
