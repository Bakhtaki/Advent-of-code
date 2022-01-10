"""
This scripts for advent of code 2021.

Level8 part2.
"""


def get_data(filename):
    """Load data from file to scipts."""
    with open(filename, 'r', encoding='utf8') as file:
        lines = file.readlines()
        outputs = [line.strip().split("|")[1] for line in lines]
    return outputs


def five_char_decoder(word):
    """Detect 5 charcter  string in between 2,3,5."""
    if ''.join(sorted(word)) == 'abcdf':
        decode = "3"
    if ''.join(sorted(word)) == 'acdfg':
        decode = "2"
    if ''.join(sorted(word)) == 'bcdef':
        decode = "5"

    return decode


def six_char_decoder(word):
    """Detect 6 charchter string between 0,6,9."""
    if ''.join(sorted(word)) == 'abcdeg':
        decode = '0'
    if ''.join(sorted(word)) == 'bcdefg':
        decode = '6'
    if ''.join(sorted(word)) == 'abcdef':
        decode = '9'
    return decode


def section_decoder(word):
    """Convert an string to related integer."""
    # Detect One
    if len(word) == 2:
        target = "1"
    # Detect Seven
    if len(word) == 3:
        target = "7"
    # Detect Four
    if len(word) == 4:
        target = '4'
    # Detect Eight
    if len(word) == 7:
        target = "8"
    # detect Len 5  which might be 2,3,5
    if len(word) == 5:
        target = five_char_decoder(word)
    # Detect len 6 which might be 0,6,9
    if len(word) == 6:
        target = six_char_decoder(word)

    return target


def decode_output(digits):
    """Determine 2,3,4,8 lemght digits."""
    total = 0
    for line in digits:
        this_line_output = ""
        line = line.split()
        for word in line:
            decoded_value = section_decoder(word)
            print(word, len(word), decoded_value)
            this_line_output += decoded_value
        total += int(this_line_output)
    return total


def main():
    """Structre of script."""
    digits = get_data("advent_of_code_l8.txt")
    total = decode_output(digits)
    print(total)


if __name__ == '__main__':
    main()
