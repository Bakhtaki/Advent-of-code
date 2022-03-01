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
        # Test 1
        input1 = 'C200B40A82'
        result1 = part2.parse(data_preparation(input1), 0)[0]
        self.assertEqual(result1, 3)

        # Test 2
        input2 = '04005AC33890'
        result2 = part2.parse(data_preparation(input2), 0)[0]
        self.assertEqual(result2, 54)

        # Test 3
        input3 = '880086C3E88112'
        result3 = part2.parse(data_preparation(input3), 0)[0]
        self.assertEqual(result3, 7)

        # Test 4
        input4 = 'CE00C43D881120'
        result4 = part2.parse(data_preparation(input4), 0)[0]
        self.assertEqual(result4, 9)

        # Test 5
        input5 = 'D8005AC2A8F0'
        result5 = part2.parse(data_preparation(input5), 0)[0]
        self.assertEqual(result5, 15)

        # Test 6
        input6 = 'F600BC2D8F'
        result6 = part2.parse(data_preparation(input6), 0)[0]
        self.assertEqual(result6, 15)

        # Test 7
        input7 = '9C005AC2F8F0'
        result7 = part2.parse(data_preparation(input7), 0)[0]
        self.assertEqual(result7, 15)


if __name__ == '__main__':
    unittest.main()
