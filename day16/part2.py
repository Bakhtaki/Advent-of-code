"""This script for Solving day 16 puzzle part 2."""


from __future__ import annotations
import datetime


def get_data(filename):
    """Read the data from the file."""
    with open(filename, "r", encoding='utf-8') as file:
        data = file.read().strip()
        data = bin(int(data, base=16))[2:]
        print('Data Has been read.')
        return data


def operation(type_id, values):
    """Calculate operation base on the given type and values."""
    # Sum for  type 0
    if type_id == 0:
        result = sum(values)

    # Multiply for type 1
    if type_id == 1:
        result = 1
        for each in values:
            result *= each

    # Minimum for type 2
    if type_id == 2:
        result = min(values)

    # Maximum for type 3
    if type_id == 3:
        result = max(values)

    # Greater Value for type 5
    if type_id == 5:
        result = 1 if values[0] > values[1] else 0

    # Lesser Value for type 6
    if type_id == 6:
        result = -1 if values[0] < values[1] else 0

    # Equal Value for type 7
    if type_id == 7:
        result = -1 if values[0] == values[1] else 0

    # return result
    return result


def parse(data, index, j=1):
    """Parse Packet to get values.

    Args:
        data (String): Binary Packet
        index (Int):  Start of packet
        j (int, optional): _description_. Defaults to 1.
    """
    if index == j:
        return None, None

    # Remove Useless bits
    if index > len(data) - 4:
        return None, None

    # Get version
    version = int(data[:3], base=2)

    # Get type
    type_id = int(data[3:6], base=2)

    # literal values
    if type_id == 4:
        index = 6
        end = False
        literal_value = ''
        while not end:
            if data[index] == '0':
                end = True
            literal_value += data[index+1:index+5]
            index += 5
        value = int(literal_value, base=2)
        return value, index

    # Operator Parameters
    sub_packet = []
    next_start = None

    len_id = data[index+6]

    # if Len ID is 0 next 15 bits are the length
    if len_id == '0':
        num_bits = data[index+7:index+22]
        print(int(num_bits, base=2))


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
