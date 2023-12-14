import sys


def get_file_content(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read().strip().split('\n')
    return file_content


def part1(data):

    def find_loc(seed):
        cur_num = seed

        for each in maps:
            for destination, source, range_len in each:
                if source <= cur_num <= source + range_len:
                    cur_num = destination + (cur_num - source)
                    break

        return cur_num

    seeds = list(map(int, data[0].split(' ')[1:]))
    maps = []

    i = 2

    while i < len(data):
        maps.append([])
        i += 1
        while i < len(data) and not data[i] == '':
            destination, source, range_len = map(int, data[i].split())
            maps[-1].append((destination, source, range_len))
            i += 1

        i += 1

    locs = []

    for seed in seeds:
        loc = find_loc(seed)
        locs.append(loc)

    print(f'Part 1 anwser: {min(locs)}')


def part2(data):
    print(data)


if __name__ == '__main__':
    file_name = sys.argv[1]

    data = get_file_content(file_name)
    print("Which part do you want to run?")
    input = int(input("Enter 0 for both, 1 for part 1 and 2 for part 2: "))
    if input == 0:
        part1(data)
        part2(data)

    elif input == 1:
        part1(data)

    elif input == 2:
        part2(data)
    else:
        print("Invalid input")
