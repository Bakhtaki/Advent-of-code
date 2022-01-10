"""
Advent Of code Level1.

This is level we will check how many time depth increased.
"""
pervious_line = 0
depth_increase = -1

with open("advent_of_code_l1.txt", 'w', encoding="utf-8") as file:
    lines = file.readlines()
file.close()

for line in lines:
    if int(line) > int(pervious_line):
        depth_increase += 1
        pervious_line = int(line)
    else:
        pervious_line = int(line)

print(f"Depth increased {depth_increase} times")
