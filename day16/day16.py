"""
Advent of the code 2021.

day16 part 1 and 2.
"""

from __future__ import annotations
import time


def get_data(filename):
    """Read the data from the file."""
    with open(filename, "r", encoding='utf-8') as file:
        data = file.read().strip()
        data = bin(int(data, base=16))[2:]
        print('Data Has been read.')
        return data


def parse_packet(packet, count=-1):
    """
    Parse data to packets.

    :param data: data to parse
    """
    # Check packet not empty
    if packet == '' or int(packet) == 0:
        return 0

    # check if count is 0
    if count == 0:
        return parse_packet(packet, count=-1)

    # Get Version
    version = int(packet[0:3], base=2)

    # Get Type ID
    type_id = int(packet[3:6], base=2)

    # Determine Type
    # Literal Value
    if type_id == 4:
        i = 6
        literal_value = ''
        end = False
        while not end:
            if packet[i] == '0':
                end = True
            literal_value += packet[i+1:i+5]
            i += 5

        value = int(literal_value, base=2)
        return version + parse_packet(packet[i:], count-1)

    # otherwise it's a pointer
    length_pointer = packet[6]

    # Length pointer is 0
    if length_pointer == '0':
        # Check Next 15 bits
        number_of_bits = int(packet[7:22], base=2)
        return version + parse_packet(packet[22:22+number_of_bits], -1) +\
            parse_packet(packet[22+number_of_bits:], count-1)
    else:
        # Check nex 11 bits
        number_of_packets = int(packet[7:18], base=2)
        return version + parse_packet(packet[18:], count=number_of_packets)


def main():
    """Prepartion To pass data to other sections."""
    # save start time
    start_time = time.time()

    # get data
    data = get_data("day16.txt")

    # Print Data Lenght
    print(f'Data length is: {len(data)}')

    # sleep for 0.5 seconds
    time.sleep(0.5)

    # zfill data to have a length multiple of 4 if not
    if len(data) % 4 != 0:
        data = data.zfill(len(data) + (4 - len(data) % 4))

    # print new data length
    print(f'Data length is: {len(data)}')
    print('data has been modified.')

    # Part 1
    # parse data to packets
    part1 = parse_packet(data)

    # Print result
    print(f'Answer for part1: {part1}')

    # Save end time
    end_time = time.time()

    # print execution time - sleep 2 seconds
    print(f'Execution time: {end_time - start_time:.3f} seconds')


if __name__ == "__main__":
    main()
    print('done')
