import boarding
import random
import unittest


class TestBoarding(unittest.TestCase):
    def test_cycles_codeStart(self):
        for code in boarding.allCodes():
            id = boarding.decode(code)
            # print("{}:{}".format(code, id))
            self.assertEqual(code, boarding.encode(id))

    def test_cycles_numStart(self):
        for i in range(2**11):
            code = boarding.encode(i)
            self.assertEqual(i, boarding.decode(code), "{}:{}".format(i, code))

    def test_decode_known0(self):
        self.assertEqual(357, boarding.decode("FBFBBFFRLR"))

    def test_decode_known1(self):
        self.assertEqual(567, boarding.decode("BFFFBBFRRR"))

    def test_decode_known2(self):
        self.assertEqual(119, boarding.decode("FFFBBBFRRR"))

    def test_decode_known3(self):
        self.assertEqual(820, boarding.decode("BBFFBBFRLL"))

    def test_encode_known0(self):
        self.assertEqual("FBFBBFFRLR", boarding.encode(357))

    def test_encode_known1(self):
        self.assertEqual("BFFFBBFRRR", boarding.encode(567))

    def test_encode_known2(self):
        self.assertEqual("FFFBBBFRRR", boarding.encode(119))

    def test_encode_known3(self):
        self.assertEqual("BBFFBBFRLL", boarding.encode(820))

    def test_encode_known4(self):
        self.assertEqual("BFBFBBBLRR", boarding.encode(699))

    def test_highestSeat_input(self):
        self.assertEqual(915, boarding.highestSeat("input.txt"))

    def test_missingSeat_input(self):
        self.assertEqual(699, boarding.missingSeat("input.txt"))


if __name__ == '__main__':
    unittest.main()


