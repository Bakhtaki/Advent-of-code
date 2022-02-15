"""
This Script is used to solve Advent of Code 2021 Day 13.

Part 1: uncomment last break in main()
part2: comment last break in main()

"""


def get_data(file_name: str):
    """Get data from file."""
    with open(file_name, 'r', encoding='utf8') as file:
        input_points, input_instruction = file.read().split('\n\n')

        points = set()
        for point in input_points.splitlines():
            x, y = point.split(',')
            points.add((int(x), int(y)))

    return points, input_instruction


def print_points(points: set[tuple[int, int]]) -> None:
    """Print points."""
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in points:
                print('#', end='')
            else:
                print('.', end='')
        print()


def main() -> None:
    """Use to control logic of script."""
    points, instruction = get_data("day13.txt")

    for line in instruction.splitlines():
        if line == '':
            continue
        else:
            line = line.split()[-1]
            axis, value = line.split('=')
            if axis == 'x':
                points = {
                    (x if x < int(value) else
                     int(value) - (int(x) - int(value)), int(y))
                    for x, y in points
                }
            elif axis == 'y':
                points = {
                    (x, y if y < int(value) else
                     int(value) - (int(y) - int(value)))
                    for x, y in points
                }
            else:
                raise ValueError(f'Unknown axis: {axis}')
        # break

    print_points(points)
    print(len(points))


if __name__ == "__main__":
    main()
    print("Done.")
