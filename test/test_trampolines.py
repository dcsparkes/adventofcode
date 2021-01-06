"""
https://adventofcode.com/2017/day/5
"""
import unittest
from _2017 import d05_trampolines


class TestTrampolines(unittest.TestCase):
    fInput = "input2017_05a.txt"
    fTest1 = "test2017_05a.txt"

    def test_readFile_fTest1_len(self):
        ba = d05_trampolines.BouncingAnt(self.fTest1)
        self.assertEqual(5, len(ba.maze))

    def test_runProgram_fTest1_len(self):
        ba = d05_trampolines.BouncingAnt(self.fTest1)
        steps = [p for p in ba.runMaze()]
        self.assertEqual(5, len(steps))

    def test_runProgram_fTest1_part2_len(self):
        ba = d05_trampolines.BouncingAnt(self.fTest1)
        steps = [p for p in ba.runMaze(dec=True)]
        self.assertEqual(10, len(steps))

    def test_runProgram_fTest1_steps(self):
        expected = [0, 0, 1, 4, 1]
        ba = d05_trampolines.BouncingAnt(self.fTest1)
        steps = [pos for _, pos in ba.runMaze()]
        self.assertEqual(expected, steps)


if __name__ == '__main__':
    unittest.main()
