import elevator
import unittest


class TestElevator(unittest.TestCase):
    def test_parenthesesCount_inputFile(self):
        self.assertEqual(74, elevator.parenthesesCount("input1.1.txt"))

    def test_parenthesesMismatch_inputFile(self):
        self.assertEqual(1795, elevator.parenthesesMismatch("input1.1.txt"))

if __name__ == '__main__':
    unittest.main()
