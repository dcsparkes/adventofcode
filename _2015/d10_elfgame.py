"""
https://adventofcode.com/2015/day/10
"""
import unittest


def round(text):
    currentChar = None
    currentCount = 0
    reply = []
    for c in text:
        if currentChar == c:
            currentCount += 1
        else:
            if currentChar:
                reply.extend([str(currentCount), currentChar])
            currentChar = c
            currentCount = 1
    reply.extend([str(currentCount), currentChar])
    return ''.join(reply)


class TestElfGame(unittest.TestCase):
    def test_round_1(self):
        self.assertEqual("11", round("1"))

    def test_round_11(self):
        self.assertEqual("21", round("11"))

    def test_round_21(self):
        self.assertEqual("1211", round("21"))

    def test_round_1211(self):
        self.assertEqual("111221", round("1211"))

    def test_rounds_1(self):
        text = "1"
        for i in range(5):
            text = round(text)
        self.assertEqual("312211", text)

    def test_rounds_full40(self):
        text = "3113322113"
        for i in range(40):
            text = round(text)
        print("Part 1: {}".format(len(text)))
        self.assertEqual(329356, len(text))

    def test_rounds_full50(self):
        text = "3113322113"
        for i in range(50):
            text = round(text)
        print("Part 2: {}".format(len(text)))
        self.assertEqual(4666278, len(text))


if __name__ == '__main__':
    unittest.main()
