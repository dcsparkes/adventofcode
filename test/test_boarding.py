import itertools
import unittest
from _2020 import d05_boarding


def allCodes():
    return [''.join(row + seat) for row in itertools.product("BF", repeat=7) for seat in itertools.product("LR", repeat=3)]

def allCodesShuffled():
    return [''.join(row + seat) for row in itertools.product("BF", repeat=7) for seat in itertools.product("LR", repeat=3)]

def encode(num):
    prefix = format(num // 8, '07b').replace('0', 'F').replace('1', 'B')
    suffix = format(num % 8, '03b').replace('0', 'L').replace('1', 'R')
    return ''.join([prefix, suffix])



class TestBoarding(unittest.TestCase):
    def test_cycles_codeStart(self):
        for code in allCodes():
            id = d05_boarding.decode(code)
            # print("{}:{}".format(code, id))
            self.assertEqual(code, encode(id))

    def test_cycles_numStart(self):
        for i in range(2**11):
            code = encode(i)
            self.assertEqual(i, d05_boarding.decode(code), "{}:{}".format(i, code))

    def test_decode_known0(self):
        self.assertEqual(357, d05_boarding.decode("FBFBBFFRLR"))

    def test_decode_known1(self):
        self.assertEqual(567, d05_boarding.decode("BFFFBBFRRR"))

    def test_decode_known2(self):
        self.assertEqual(119, d05_boarding.decode("FFFBBBFRRR"))

    def test_decode_known3(self):
        self.assertEqual(820, d05_boarding.decode("BBFFBBFRLL"))

    def test_encode_known0(self):
        self.assertEqual("FBFBBFFRLR", encode(357))

    def test_encode_known1(self):
        self.assertEqual("BFFFBBFRRR", encode(567))

    def test_encode_known2(self):
        self.assertEqual("FFFBBBFRRR", encode(119))

    def test_encode_known3(self):
        self.assertEqual("BBFFBBFRLL", encode(820))

    def test_encode_known4(self):
        self.assertEqual("BFBFBBBLRR", encode(699))

    def test_highestSeat_input(self):
        self.assertEqual(915, d05_boarding.highestSeat("../input/input2020_05a.txt"))

    def test_missingSeat_input(self):
        self.assertEqual(699, d05_boarding.missingSeat("../input/input2020_05a.txt"))


if __name__ == '__main__':
    unittest.main()


