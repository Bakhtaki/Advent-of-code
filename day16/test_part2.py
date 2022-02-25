"""Test for Part2."""

import unittest
import part2


def data_preparation(data):
    """Prepare data for testing."""
    # Convert data to binary
    data = bin(int(data, base=16))[2:]
    # Add leading zeros
    if len(data) % 4 != 0:
        data = data.zfill(len(data) + (4 - (len(data) % 4)))
    return data


class TestPart2(unittest.TestCase):
    """Test for Part2."""

    def test_part2(self):
        """Test part2."""
        input1 = 'C200B40A82'
        input2 = '04005AC33890'
        input3 = '880086C3E88112'
        input4 = 'CE00C43D881120'
        input5 = 'D8005AC2A8F0'
        input6 = 'F600BC2D8F'
        input7 = '9C005AC2F8F0'

        # Result
        resault = part2.parse(data_preparation(input1), 0)[0]
        # Check result
        self.assertEqual(resault, 3)

        # Result
        resault = part2.parse(data_preparation(input2), 0)[0]
        # Check result
        self.assertEqual(resault, 54)

        # Result
        resault = part2.parse(data_preparation(input3), 0)[0]
        # Check result
        self.assertEqual(resault, 7)

        # Result
        resault = part2.parse(data_preparation(input4), 0)[0]
        # Check result
        self.assertEqual(resault, 9)

        # Result
        resault = part2.parse(data_preparation(input5), 0)[0]
        # Check result
        self.assertEqual(resault, 15)

        # Result
        resault = part2.parse(data_preparation(input6), 0)[0]
        # Check result
        self.assertEqual(resault, 15)

        # Result
        resault = part2.parse(data_preparation(input7), 0)[0]
        # Check result
        self.assertEqual(resault, 15)


if __name__ == '__main__':
    unittest.main()
