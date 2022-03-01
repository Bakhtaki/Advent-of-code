"""Solution for Advent of Code day 17."""

import datetime


def get_data(filename: str) -> list:
    """Get data from file."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        _x, _y, x_area, y_area = data.split()
        x_area = x_area[2:-1]
        y_area = y_area[2:]

        x1, x2 = x_area.split('..')
        y1, y2 = y_area.split('..')

    return int(x1), int(x2), int(y1), int(y2)


def main() -> None:
    """Compute solution."""
    x1, x2, y1, y2 = get_data('day17_test.txt')
    print(f'Test: {x1} {x2} {y1} {y2}')


if __name__ == '__main__':
    # Save start time of program
    start_time = datetime.datetime.now()

    main()

    # Save end time of program
    end_time = datetime.datetime.now()

    # Print the execution time
    print('Duration:', end_time - start_time)
