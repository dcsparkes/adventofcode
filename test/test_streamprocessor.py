"""
https://adventofcode.com/2017/day/9
"""
import unittest
from _2017 import d09_streamprocessing


class TestStateMachine(unittest.TestCase):
    def test_inject_singleBraces(self):
        sm = d09_streamprocessing.StateMachine()
        for char in '{}':
            sm.inject(char)
        self.assertEqual(1, sm.runningTotal)

    def test_inject_nestedBraces(self):
        sm = d09_streamprocessing.StateMachine()
        for char in '{{{}}}':
            sm.inject(char)
        self.assertEqual(6, sm.runningTotal)

    def test_inject_branchingBraces(self):
        sm = d09_streamprocessing.StateMachine()
        for char in '{{{},{},{{}}}}':
            sm.inject(char)
        self.assertEqual(16, sm.runningTotal)

    def test_inject_garbageBraces(self):
        sm = d09_streamprocessing.StateMachine()
        for char in '{<a>,<a>,<a>,<a>}':
            sm.inject(char)
        self.assertEqual(1, sm.runningTotal)

    def test_inject_nestedGarbageBraces(self):
        sm = d09_streamprocessing.StateMachine()
        for char in '{{<ab>},{<ab>},{<ab>},{<ab>}}':
            sm.inject(char)
        self.assertEqual(9, sm.runningTotal)

    def test_inject_bangedNestedBraces(self):
        sm = d09_streamprocessing.StateMachine()
        for char in '{{<!!>},{<!!>},{<!!>},{<!!>}}':
            sm.inject(char)
        self.assertEqual(9, sm.runningTotal)

    def test_inject_bangededGarbageBraces(self):
        sm = d09_streamprocessing.StateMachine()
        for char in '{{<a!>},{<a!>},{<a!>},{<ab>}}':
            sm.inject(char)
        self.assertEqual(3, sm.runningTotal)


if __name__ == '__main__':
    unittest.main()
