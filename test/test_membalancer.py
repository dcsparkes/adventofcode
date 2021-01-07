"""
https://adventofcode.com/2017/day/6
"""
import unittest
from _2017 import d06_memreallocation


class TestMemBalancer(unittest.TestCase):
    fInput = "input2017_06a.txt"
    fTest1 = "test2017_06a.txt"

    def test_readFile_fTest1_len(self):
        mb = d06_memreallocation.MemBalancer(self.fTest1)
        self.assertEqual(4, len(mb.memState))

    def test_readFile_fTest1_state(self):
        mb = d06_memreallocation.MemBalancer(self.fTest1)
        self.assertEqual([0, 2, 7, 0], mb.memState)

    def test_rebalance_0270(self):
        mb = d06_memreallocation.MemBalancer()
        mb.memState = [0, 2, 7, 0]
        mb._rebalance()
        expected = [2, 4, 1, 2]
        self.assertEqual(expected, mb.memState)

    def test_rebalance_2412(self):
        mb = d06_memreallocation.MemBalancer()
        mb.memState = [2, 4, 1, 2]
        mb._rebalance()
        expected = [3, 1, 2, 3]
        self.assertEqual(expected, mb.memState)

    def test_rebalance_3123(self):
        mb = d06_memreallocation.MemBalancer()
        mb.memState = [3, 1, 2, 3]
        mb._rebalance()
        expected = [0, 2, 3, 4]
        self.assertEqual(expected, mb.memState)

    def test_rebalance_0234(self):
        mb = d06_memreallocation.MemBalancer()
        mb.memState = [0, 2, 3, 4]
        mb._rebalance()
        expected = [1, 3, 4, 1]
        self.assertEqual(expected, mb.memState)

    def test_rebalance_1341(self):
        mb = d06_memreallocation.MemBalancer()
        mb.memState = [1, 3, 4, 1]
        mb._rebalance()
        expected = [2, 4, 1, 2]
        self.assertEqual(expected, mb.memState)

    def test_balance_fInput_count(self):
        mb = d06_memreallocation.MemBalancer(self.fInput)
        self.assertEqual(7864, mb.balance()[0])

    def test_balance_fInput_interim(self):
        mb = d06_memreallocation.MemBalancer(self.fInput)
        count, last = mb.balance()
        self.assertEqual(1695, count - last)

    def test_balance_fTest1_count(self):
        mb = d06_memreallocation.MemBalancer()
        mb.memState = [0, 2, 7, 0]
        self.assertEqual(5, mb.balance()[0])

    def test_balance_fTest1_interim(self):
        mb = d06_memreallocation.MemBalancer()
        mb.memState = [0, 2, 7, 0]
        count, last = mb.balance()
        self.assertEqual(4, count - last)


if __name__ == '__main__':
    unittest.main()
