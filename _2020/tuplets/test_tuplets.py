import unittest
import tuplets

class MyTestCase(unittest.TestCase):
    def test_findPair(self):
        (a, b) = tuplets.findPair(2020, "input.txt")
        self.assertEqual(a * b, 935419, "{} * {} = {}".format(a, b, a * b))

    def test_findTriplet(self):
        (c, d, e) = tuplets.findTriplet(2020, "input.txt")
        self.assertEqual(c * d * e, 49880012, "{} * {} * {} = {}".format(c, d, e, c * d * e))


if __name__ == '__main__':
    unittest.main()
