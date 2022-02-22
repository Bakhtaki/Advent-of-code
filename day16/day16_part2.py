"""This script for Solving day 16 puzzle part 2."""


from __future__ import annotations
import datetime
import time


def get_data(filename):
    """Read the data from the file."""
    with open(filename, "r", encoding='utf-8') as file:
        data = file.read().strip()
        data = bin(int(data, base=16))[2:]
        print('Data Has been read.')
        return data


def main():
    """Main Structure of script."""
    # Save Start Time
    start_time = datetime.datetime.now()

    # Get Data
    data = get_data('day16_test.txt')

    # zfill data for multiple to 4 bits
    if len(data) % 4 != 0:
        data = data.zfill(len(data) + (4 - len(data) % 4))

    # Save End Time
    end_time = datetime.datetime.now()

    # Print Time
    print(f'Time Taken: {end_time - start_time}')


if __name__ == '__main__':
    main()
