"""Solution for advent of code 2022 day 5."""

from os import stat
import sys


# Function to read input_file
def read_input(input_file):
    """Read input file."""
    with open(input_file, "r", encoding='utf-8') as file:
        section1, section2 = file.read().split("\n\n")
    return section1, section2


# Function to solve part one
def solve_part_one(state, structs):
    """Solve part one."""
    reshaped_state = ""
    output = ""
    # print state line by line reversed
    for line in state.splitlines()[::-1]:
        reshaped_state += line + "\n"

    # Remove First line as header
    header = reshaped_state.splitlines()[0]

    # Remove header from state
    state = reshaped_state.replace(header, "")
    # Remove first empty line
    state = state.replace("\n", "", 1)
    # print(state)

    # Convert header to list
    header = header.split(" ")
    num_stacks = int(max(header))
    # print(f'num_stacks: {num_stacks}')

    # Initialize stacks.
    stacks = [[] for _ in range(num_stacks)]

    # get the count of lines in state
    num_lines = len(state.splitlines())
    # print(f'num_lines: {num_lines}')

    state = state.split('\n')
    for i in range(num_lines):
        line = state[i]
        boxes = line[1::4]
        for j in range(len(boxes)):
            if boxes[j] != ' ':
                stacks[j].append(boxes[j])

    # Operate the structs
    for struct in structs.splitlines():
        struct = struct.split(" ")
        qty, src, dest = int(struct[1]), int(struct[3]), int(struct[5])

        src -= 1
        dest -= 1

        for _ in range(qty):
            stacks[dest].append(stacks[src].pop())

    # Print last element of each stacks
    for stack in stacks:
        output += stack[-1] + ""

    print(f'Part one: {output}')

    # return some variables to use in part two
    return state, num_stacks, num_lines


# Function to solve part two
def solve_part_two(state, num_stacks, num_lines,prod_rules):
    """Solve Part two."""
    stacks = [[] for _ in range(num_stacks)]
    output = ""

    for i in range(num_lines):
        line = state[i]
        boxes = line[1::4]
        for j in range(len(boxes)):
            if boxes[j] != ' ':
                stacks[j].append(boxes[j])

    for rule in prod_rules.splitlines():
        rule = rule.split(" ")
        qty, src, dest = int(rule[1]), int(rule[3]), int(rule[5])

        src -= 1
        dest -= 1

        # separate last qty elements from src stack.
        last_qty = stacks[src][-qty:]
        stacks[src] = stacks[src][:-qty]
        stacks[dest] += last_qty

    # Print last element of each num_stacks
    for stack in stacks:
        output += stack[-1] + ""

    print(f'Part two: {output}')


if __name__ == "__main__":
    input_arg_1 = sys.argv[1]
    init_state, prod_rules = read_input(input_arg_1)

    # Part one
    init_state, num_stack, num_lines = solve_part_one(init_state, prod_rules)

    # Part two
    solve_part_two(init_state, num_stack, num_lines, prod_rules)
