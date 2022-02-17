"""
Advent of the code 2021.

day16 part 1 and 2.
"""

from __future__ import annotations
import time


def get_data(filename):
    """
    Read the data from the file.
    """
    with open(filename, "r", encoding='utf-8') as file:
        data = file.read().strip()
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
    version = int(packet[:3], base=2)

    # Get Type ID
    type_id = int(packet[3:6], base=2)




def main():
    """Main function. """
    # save start time
    start_time = time.time()

    # get data
    data = get_data("day16.txt")

    # Print Data Lenght
    print(f'Data length is: {len(data)}')

    # sleep for 0.5 seconds
    time.sleep(0.5)

    # zfill data to have a length multiple of 4
    data = data.zfill(len(data) + (4 - len(data) % 4))

    # print new data length
    print(f'Data length is: {len(data)}')

    # Part 1
    # parse data to packets
    parse_packet(data)

    # Save end time
    end_time = time.time()

    # print execution time - sleep 2 seconds
    print(f'Execution time: {end_time - start_time:.3f} seconds')


if __name__ == "__main__":
    main()
    print('done')
