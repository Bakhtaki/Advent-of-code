"""
This is script for code 2021 competition.

Level 3 part 2
"""
oxygen_generator_rating = ''
scrubber_ratig = ''
criteria_bit = ""


with open('advent_of_code_l3.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    file.close()
loop = len(lines[0])
lines_Prime = lines
for i in range(loop):
    zero_count = 0
    one_count = 0
    for line in lines_Prime:
        check = line[i]
        if check == "1":
            one_count += 1
        if check == '0':
            zero_count += 1
    # print(f'{one_count} ones and {zero_count}zero in list in bit {i}')
    if zero_count > one_count:
        criteria_bit = "0"
    else:
        criteria_bit = '1'
    # print(f'criteria_bit is :{criteria_bit}')
    temp = []
    for line in lines_Prime:
        if line[i] == criteria_bit:
            temp.append(line)
    lines_Prime = temp
    # print(f'lenght list is decreased to {len(lines_Prime)}')
    # print(lines_Prime)
    if len(lines_Prime) == 1:
        oxygen_generator_rating = lines_Prime[0]
        print(f'oxygen_generator_rating :{oxygen_generator_rating}')
        break
lines_Prime = lines
for i in range(loop):
    zero_count = 0
    one_count = 0
    for line in lines_Prime:
        check = line[i]
        if check == "1":
            one_count += 1
        if check == '0':
            zero_count += 1
    # print(f'{one_count} ones and {zero_count} zero in list in bit {i}')
    if one_count < zero_count:
        criteria_bit = "1"
    else:
        criteria_bit = '0'
    # print(f'criteria_bit is :{criteria_bit}')
    temp = []
    for line in lines_Prime:
        if line[i] == criteria_bit:
            temp.append(line)
    lines_Prime = temp
    # print(f'lenght list is decreased to {len(lines_Prime)}')
    # print(lines_Prime)
    if len(lines_Prime) == 1:
        scrubber_ratig = lines_Prime[0]
        print(f'scrubber_ratig :{scrubber_ratig}')
        break
print("answer is : ")
print(int(oxygen_generator_rating, 2) * int(scrubber_ratig, 2))
