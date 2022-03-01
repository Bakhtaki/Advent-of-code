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
        result = 1 if values[0] < values[1] else 0

    # Equal Value for type 7
    if type_id == 7:
        result = 1 if values[0] == values[1] else 0

    # return result
    return result


def parse(data, i, j=1):
    """Parse Packet to get values.

    Args:
        data (String): Binary Packet
        index (Int):  Start of packet
        j (int, optional): _description_. Defaults to 1.
    """
    if i == j:
        return None, None

    # Ending bits
    if i + 4 > len(data):
        return None, None

    # Get Version
    version = int(data[i:i+3], base=2)

    # Get Type
    type_id = int(data[i+3:i+6], base=2)

    # Literal Packet
    if type_id == 4:
        i += 6
        num_str = ''
        end = False
        while not end:
            if data[i] == '0':
                end = True
            num_str += data[i+1:i+5]
            i += 5
        value = int(num_str, base=2)
        return value, i

    # Operator Packet
    sub_packets = []
    next_start = None  # Value to return

    # Detect type of packet
    len_id = data[i+6]

    # parse if len_id shows length of packet
    if len_id == '0':
        # Next 15 bits represents how many bits are inside the packet
        num_bits = int(data[i+7:i+22], base=2)

        end = i + 22 + num_bits
        index = i + 22
        prev_index = None

        while index != None:
            prev_index = index
            value, index = parse(data, index, j=end)
            sub_packets.append(value)
        sub_packets = sub_packets[:-1]  # Remove last None
        next_start = prev_index

    # parse if len_id shows number of packets
    else:
        # Next 11 bits represents how many packets are inside
        rem_sub_packets = int(data[i+7:i+18], base=2)
        index = i + 18
        while rem_sub_packets > 0:
            value, index = parse(data, index)
            rem_sub_packets = -1
            sub_packets.append(value)
        next_start = index

    # Proccess the Operations
    return operation(type_id, sub_packets), next_start


def main():
    """Structure of script."""
    # Save Start Time
    start_time = datetime.datetime.now()

    # Get Data
    data = get_data('day16_test.txt')

    # zfill data for multiple to 4 bits
    if len(data) % 4 != 0:
        data = data.zfill(len(data) + (4 - len(data) % 4))

    answer = parse(data, 0)[0]

    # Print Answer
    print(f'Answer: {answer}')

    # Save End Time
    end_time = datetime.datetime.now()

    # Print Time
    print(f'Time Taken: {end_time - start_time}')


if __name__ == '__main__':
    main()
