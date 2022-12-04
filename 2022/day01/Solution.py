"""Advent of Code 2022 Day 1: Solution."""


# Define Function to read input file
def read_input(filename):
    """Read input file and return list of integers."""
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read().splitlines()
    return data


# Define Function to solve part 1
def part1(data):
    """Solve part 1."""
    result = []
    sum = 0

    for element in data:
        if element == "":
            result.append(sum)
            sum = 0
        else:
            sum += int(element)
    result.append(sum)

    return result


# Define Main Function
def main():
    """Main Program."""
    # Read input file
    data = read_input("input1.txt")

    # Solve part part1
    result = part1(data)

    # Print result for part part1
    print("Part 1: {}".format(max(result)))

    # Part 2 Solution
    # Sort result reverse
    result = sorted(result, reverse=True)

    # Sum first 3 elements
    print("Part 2: {}".format(result[0] + result[1] + result[2]))


# Run Program
if __name__ == "__main__":
    main()
