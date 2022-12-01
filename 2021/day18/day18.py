"""
This is script for Advent of Code 2018 Day 18.

Part One
"""

# Import the necessary modules
import datetime


# Get data  from file
def get_data(filename):
    """Get data from file."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    return data


# Define Node Class
class Node:
    """Node class."""

    def __init__(self, value=None):
        """Initialize node."""
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        """Return string representation of node."""
        return f'[{str(self.left), str(self.right)}]'


# Define Parse function
def parse(data):
    """Parse data."""
    root = Node()
    if isinstance(data, int):
        root.value = data
        return root

    root.left = parse(data[0])
    root.right = parse(data[1])
    root.left.parent = root
    root.right.parent = root

    reduce_tree(root)
    return root


# Define reduce_tree function
def reduce_tree(root):
    """Reduce Tree function."""



# Define Add Snailfish
def add_pair(pair1, pair2):
    """Add pair of numbers."""
    root = Node()
    root.left = pair1
    root.right = pair2
    root.left.parent = root
    root.right.parent = root
    reduce_tree(root)
    return root


# Define Magnitude function
def magnitude(root):
    """Return magnitude of data."""
    if isinstance(root, int):
        return root

    return 3 * magnitude(root.left) + 2 * magnitude(root.right)


# Main function
def main():
    """Flow of the script."""
    data = get_data('day18_test.txt')
    print(f'data: {data}')


if __name__ == '__main__':
    # Save Start time
    start_time = datetime.datetime.now()

    # Call main function
    main()

    # Save execution time
    end_time = datetime.datetime.now()
    print(f'Execution Time: {end_time - start_time}')
