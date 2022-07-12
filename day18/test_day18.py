"""
This is  script for test day 18 functions.

functions to test : add_pairs, magnitude, split_data, explode
"""
import unittest
from day18 import explode, split_data, add_pairs, magnitude


class Test(unittest.TestCase):
    """Test functions."""

    def test_explode(self):
        """Test explode function."""
        data = '..^^.'
        expected = '..^^.'
        self.assertEqual(explode(data), expected)

    def test_split_data(self):
        """Test split_data function."""
        data = '..^^.'
        expected = ['..', '^^.']
        self.assertEqual(split_data(data), expected)

    def test_add_pairs(self):
        """Test add_pairs function."""
        pair1 = [1,2]
        pair2 = [[3,4],5]
        expected = [[1,2], [[3,4],5]]
        self.assertEqual(add_pairs(pair1, pair2), expected)

    def test_magnitude(self):
        """Test magnitude function."""
        pairs = ['..^^', '..^^']
        expected = 2
        self.assertEqual(magnitude(pairs), expected)


if __name__ == '__main__':
    unittest.main()
