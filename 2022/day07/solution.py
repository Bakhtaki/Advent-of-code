"""Advent of code 2022 day 7 solution."""

import sys
from collections import defaultdict
from functools import lru_cache

# Function to read input file
def read_input(input_file):
    """Read input file."""
    with open(input_file, "r", encoding='utf-8') as file:
        file_content = file.read()
    return file_content


# Function to solve part 1
def solve_part_1(input_data):
    """Solve part 1."""
    # Split input data into blocks where start with $
    blocks = input_data.split("\n$ ")
    blocks[0] = blocks[0][2:]
    # Create list to store path
    path = []

    # Create defaultdict to directory size
    directory_size = defaultdict(int)

    # Create defaultdict to directory children
    directory_children = defaultdict(list)

    # Define function to parse blocks
    def parse_block(block):
        """Parse a block of commands."""
        block_lines = block.splitlines()
        command = block_lines[0]
        output = block_lines[1:]

        # Extract Command parts
        command_parts = command.split(" ")
        operation = command_parts[0]
        # if Command is change directory
        if operation == "cd":
            # if command to change directory is ..
            if command_parts[1] == "..":
                # Remove last element from path
                path.pop()
            # if command to change directory
            else:
                # Add element to path
                path.append(command_parts[1])
            return

        # absolute path
        absolute_path = "/".join(path)

        # assert operation is list directory
        assert operation == "ls"

        sizes = []

        # for each line in output
        for line in output:
            # check if line starts with DIR
            if not line.startswith("dir"):
                # Append size to sizes
                sizes.append(int(line.split(" ")[0]))
            else:
                # Extract directory name
                directory_name = line.split(" ")[1]
                # Append directory name to directory children
                directory_children[absolute_path].append(
                        f"{absolute_path}/{directory_name}")
        directory_size[absolute_path] = sum(sizes)

    # Loop over block_lines
    for block in blocks:
        parse_block(block)

    # DFS on directory_size
    @lru_cache(None)
    def dfs(abs_path):
        """DFS on directory size."""
        size = directory_size[abs_path]
        for child in directory_children[abs_path]:
            size += dfs(child)
        return size

    answer = 0
    for abs_path in directory_size:
        if dfs(abs_path) <= 100000:
            answer += directory_size[abs_path]

    print(f"Part 1 answer: {answer}")

if __name__ == "__main__":
    # Read input file
    data = read_input(sys.argv[1])

    # Solve part One
    print("Part One: ")
    solve_part_1(data)
