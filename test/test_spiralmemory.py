from _2017 import d03_spiralmemory
import unittest


class TestSpiralMemory(unittest.TestCase):
    def test_identifyRingFuncs_comparative(self):
        for i in range(1, 121096, 3):
            self.assertEqual(d03_spiralmemory.identifyRingMathematical(1), d03_spiralmemory.identifyRingIterative(1),
                             "Failed at: {}".format(i))

    def test_identifyRing_0(self):
        self.assertEqual(0, d03_spiralmemory.identifyRing(1))

    def test_identifyRing_1(self):
        expected = [1] * 8
        ringIDs = [d03_spiralmemory.identifyRing(i) for i in range(2, 10)]
        self.assertEqual(expected, ringIDs)

    def test_identifyRing_2(self):
        expected = [2] * 16
        ringIDs = [d03_spiralmemory.identifyRing(i) for i in range(10, 26)]
        self.assertEqual(expected, ringIDs)

    def test_identifyRing_3(self):
        expected = [3] * 24
        ringIDs = [d03_spiralmemory.identifyRing(i) for i in range(26, 50)]
        self.assertEqual(expected, ringIDs)

    def test_identifyRingIterative_0(self):
        self.assertEqual(0, d03_spiralmemory.identifyRingIterative(1))

    def test_identifyRingIterative_1(self):
        expected = [1] * 8
        ringIDs = [d03_spiralmemory.identifyRingIterative(i) for i in range(2, 10)]
        self.assertEqual(expected, ringIDs)

    def test_identifyRingIterative_2(self):
        expected = [2] * 16
        ringIDs = [d03_spiralmemory.identifyRingIterative(i) for i in range(10, 26)]
        self.assertEqual(expected, ringIDs)

    def test_identifyRingIterative_3(self):
        expected = [3] * 24
        ringIDs = [d03_spiralmemory.identifyRingIterative(i) for i in range(26, 50)]
        self.assertEqual(expected, ringIDs)

    def test_spiralDistance_1(self):
        self.assertEqual(0, d03_spiralmemory.spiralDistance(1))

    def test_spiralDistance_4(self):
        self.assertEqual(1, d03_spiralmemory.spiralDistance(4))

    def test_spiralDistance_9(self):
        self.assertEqual(2, d03_spiralmemory.spiralDistance(9))

    def test_spiralDistance_12(self):
        self.assertEqual(3, d03_spiralmemory.spiralDistance(12))

    def test_spiralDistance_23(self):
        self.assertEqual(2, d03_spiralmemory.spiralDistance(23))

    def test_spiralDistance_1024(self):
        self.assertEqual(31, d03_spiralmemory.spiralDistance(1024))

    def test_spiralDistance_368078(self):
        self.assertEqual(371, d03_spiralmemory.spiralDistance(368078))

if __name__ == '__main__':
    unittest.main()
