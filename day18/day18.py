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


# Explode the data
def explode(data):
    """Explode the data."""
    pass


# Split the elements if bigger than 10
def split_data(data):
    """Split data."""
    pass


# Add pairs
def add_pairs(pair1, pair2):
    """Add pairs."""
    pass


# Calculate the magnitudes recursively
def magnitude(pairs):
    """Magnitude."""
    pass


# Main function
def main():
    """Main function."""
    data = get_data('day18.txt')
    print(f'data: {data}')


if __name__ == '__main__':
    # Save Start time
    start_time = datetime.datetime.now()

    # Call main function
    main()

    # Save execution time
    end_time = datetime.datetime.now()
    print(f'Execution Time: {end_time - start_time}')
