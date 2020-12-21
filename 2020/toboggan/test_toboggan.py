import unittest
import toboggan


class TestToboggan(unittest.TestCase):
    def test_testInput_default(self):
        self.assertEqual(7, toboggan.traverse("test.txt"))

    def test_testInput_slope0(self):
        self.assertEqual(2, toboggan.traverse("test.txt", (1, 1)))

    def test_testInput_slope1(self):
        self.assertEqual(7, toboggan.traverse("test.txt", (1, 3)))

    def test_testInput_slope2(self):
        self.assertEqual(3, toboggan.traverse("test.txt", (1, 5)))

    def test_testInput_slope3(self):
        self.assertEqual(4, toboggan.traverse("test.txt", (1, 7)))

    def test_testInput_slope4(self):
        self.assertEqual(2, toboggan.traverse("test.txt", (2, 1)))

    def test_Input_default(self):
        self.assertEqual(254, toboggan.traverse("input.txt"))

    def test_Input_slope0(self):
        self.assertEqual(63, toboggan.traverse("input.txt", (1, 1)))

    def test_Input_slope1(self):
        self.assertEqual(254, toboggan.traverse("input.txt", (1, 3)))

    def test_Input_slope2(self):
        self.assertEqual(62, toboggan.traverse("input.txt", (1, 5)))

    def test_Input_slope3(self):
        self.assertEqual(56, toboggan.traverse("input.txt", (1, 7)))

    def test_Input_slope4(self):
        self.assertEqual(30, toboggan.traverse("input.txt", (2, 1)))


    def test_Input_multipleSlopes(self):
        multiple = toboggan.traverse("input.txt", (1, 1))
        multiple *= toboggan.traverse("input.txt", (1, 3))
        multiple *= toboggan.traverse("input.txt", (1, 5))
        multiple *= toboggan.traverse("input.txt", (1, 7))
        multiple *= toboggan.traverse("input.txt", (2, 1))
        self.assertEqual(30, multiple)

if __name__ == '__main__':
    unittest.main()
