"""
Advent Of code Level2.

This is level we will check how many time depth increased
with 3 level group stages.
"""
steps = []
previous_step = 0
deptht_increase = -1

with open("advent_of_code_l1.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    file.close()


for i in range(len(lines) - 2):
    sum = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
    steps.append(sum)

print(steps)
print(len(steps))

for step in steps:
    if int(step) > int(previous_step):
        deptht_increase += 1
        previous_step = int(step)
    else:
        previous_step = int(step)

print(f"depth icreased {deptht_increase} times")
