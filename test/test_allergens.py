"""
https://adventofcode.com/2020/day/21
"""

import itertools
import unittest
from allergens import allergens


class TestAllergens(unittest.TestCase):
    fInput = "input2020_21a.txt"
    fTest = "test2020_21a.txt"

    def test_readFile_fTest(self):
        aa = allergens.Allergens()
        aa.readFile(self.fTest)
        self.assertEqual(5, aa.part1)

    def test_readFile_fInput(self):
        aa = allergens.Allergens()
        aa.readFile(self.fInput)
        self.assertEqual(2734, aa.part1)



if __name__ == '__main__':
    unittest.main()
