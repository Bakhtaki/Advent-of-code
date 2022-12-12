"""Advent of code 2022 day 11 solution."""
import sys


class Monkey:
    """Monkey class."""
    def __init__(self, items, operation, tests):
        """Object initialization."""
        self.items = items
        self.operation = operation
        self.tests = tests
        self.inspection_counter = 0

    def __repr__(self):
        """Object representation."""
        return f"Monkey({self.items}, {self.operation}, {self.tests})"


# operations
def calc(operation, num):
    """Calculate operation."""
    left, operatot, right = operation
    assert left == "old"

    if operatot == "+":
        return num + int(right)
    else:
        if right == "old":
            return num * num
        else:
            return num * int(right)


# DeFine Part 1 functions
def part1(monkeys: list) -> None:
    """Part 1 solution."""
    len_monkeys = len(monkeys)

    for round in range(20):
        for _i in range(len_monkeys):
            monkey = monkeys[_i]
            for item in monkey.items:
                item = calc(monkey.operation, item)
                item //= 3

                mod, true_case, false_case = monkey.tests
                if item % mod == 0:
                    monkeys[true_case].items.append(item)
                else:
                    monkeys[false_case].items.append(item)

                # increase inspection inspection_counter
                monkey.inspection_counter += 1

            # remove items
            monkey.items = []

    inspection_counter = [monkey.inspection_counter for monkey in monkeys]
    sorted_inspection_counter = sorted(inspection_counter)
    answer = sorted_inspection_counter[-1] * sorted_inspection_counter[-2]
    print(f"Part 1 answer: {answer}")


if __name__ == "__main__":
    with open(sys.argv[1], encoding='utf-8') as file:
        data = file.read().strip()
        parts = data.split('\n\n')
    monkeys = []

    for i, part in enumerate(parts):
        lines = part.splitlines()
        items = list(map(int, lines[1][2:].split(" ", 2)[2].split(", ")))
        operations = lines[2][2:].split(" ", 3)[3].split(" ")
        # Parse the test cases
        mode = int(lines[3][2:].split(" ")[-1])
        true_case = int(lines[4][2:].split(" ")[-1])
        false_case = int(lines[5][2:].split(" ")[-1])

        # Capsule the test cases
        tests = [mode, true_case, false_case]
        # Create the monkeys with Monkey Class
        monkeys.append(Monkey(items, operations, tests))

    # part 1
    part1(monkeys)


