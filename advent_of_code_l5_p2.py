"""
This Scripts Solution for advent of code 2021.

Level5 Part1.
"""
# import pprint as pp

filtered_lines = []
right = []
left = []
counter = 0

with open('advent_of_code_l5.txt', 'r', encoding='utf_8') as file:
    lines = file.readlines()
    lines = [line.strip().split("->") for line in lines]
file.close()

for line in lines:
    left.append(line[0].strip().split(','))
    right.append(line[1].strip().split(','))

for i in range(len(left)):
    for j in range(2):
        left[i][j] = int(left[i][j])
        right[i][j] = int(right[i][j])

max_left = max(max(left))
max_right = max(max(right))
maximum = max(max_left, max_right)

coordinates = [[0 for i in range(maximum+1)] for j in range(maximum+1)]
# pp.pprint(coordinates)

for i in range(len(left)):
    if (int(left[i][0]) == int(right[i][0])):  # Vertical
        x = left[i][0]
        y_1 = left[i][1]
        y_2 = right[i][1]
        if y_2 > y_1:
            for j in range(y_1, y_2+1):
                coordinates[j][x] += 1
        if y_1 > y_2:
            for j in range(y_2, y_1+1):
                coordinates[j][x] += 1

    if (int(left[i][1])) == int(right[i][1]):  # Horizantal
        y = left[i][1]
        x_1 = left[i][0]
        x_2 = right[i][0]
        if x_2 > x_1:
            for k in range(x_1, x_2+1):
                coordinates[y][k] += 1
        if x_1 > x_2:
            for k in range(x_2, x_1+1):
                coordinates[y][k] += 1
    #  Digonal
    if abs(int(left[i][0]) -
       int(right[i][0])) == abs(int(left[i][1]) - int(right[i][1])):
        # print(left[i], right[i])
        # increase X , Decrease Y
        if (int(left[i][0]) -
           int(right[i][0])) < (int(left[i][1]) - int(right[i][1])):
            x_1 = left[i][0]
            y_1 = left[i][1]
            x_2 = right[i][0]
            y_2 = right[i][1]
            diff = abs(x_1 - x_2)
            for j in range(diff+1):
                coordinates[y_1-j][x_1+j] += 1
        #  Decrease X , Increase Y
        if (int(left[i][0]) -
           int(right[i][0])) > (int(left[i][1]) - int(right[i][1])):
            x_1 = left[i][0]
            y_1 = left[i][1]
            x_2 = right[i][0]
            y_2 = right[i][1]
            diff = abs(x_1 - x_2)
            for j in range(diff+1):
                coordinates[y_1+j][x_1-j] += 1
        # Both in Same Direction
        if (int(left[i][0]) -
           int(right[i][0])) == (int(left[i][1]) - int(right[i][1])):
            if right[i][0] - left[i][0] < 0:
                x_1 = left[i][0]
                y_1 = left[i][1]
                x_2 = right[i][0]
                y_2 = right[i][1]
                diff = abs(x_1 - x_2)
                for j in range(diff+1):
                    coordinates[y_1-j][x_1-j] += 1
            if right[i][0] - left[i][0] > 0:
                x_1 = left[i][0]
                y_1 = left[i][1]
                x_2 = right[i][0]
                y_2 = right[i][1]
                diff = abs(x_1 - x_2)
                for j in range(diff+1):
                    coordinates[y_1+j][x_1+j] += 1

for y in range(len(coordinates)):
    for x in range(len(coordinates)):
        if coordinates[x][y] >= 2:
            counter += 1
print(counter)
