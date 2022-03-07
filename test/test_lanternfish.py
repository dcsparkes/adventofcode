"""
https://adventofcode.com/2021/day/6
"""
import unittest

from base import base
from lanternfish import lanternfish


class TestPopTrackerInternals(unittest.TestCase):
    def test_init_0(self):
        p = lanternfish.popTracker(initialTimer=0)
        self.assertEqual({0: 1}, p.pops)

    def test_tick_0(self):
        p = lanternfish.popTracker(initialTimer=0)
        p._tick()
        self.assertEqual({6: 1, 8: 1}, p.pops)

    def test_init_1(self):
        p = lanternfish.popTracker(initialTimer=1)
        self.assertEqual({1: 1}, p.pops)

    def test_tick_1(self):
        p = lanternfish.popTracker(initialTimer=1)
        p._tick()
        self.assertEqual({0: 1}, p.pops)


class TestPopTrackerResults(unittest.TestCase):
    fInput = "input2021_06a.txt"
    initialTimers = list(base.getInputLines(fInput, delimiter=','))

    def test_init_0_count(self):
        p = lanternfish.popTracker(initialTimer=0)
        self.assertEqual(1, p.count())

    def test_tick_0_count(self):
        p = lanternfish.popTracker(initialTimer=0)
        p._tick()
        self.assertEqual(2, p.count())

    def test_trackSinglePop(self):
        p = lanternfish.popTracker(initialTimer=0)
        pops = p.trackSinglePop(18)
        self.assertEqual([1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 7, 7], list(pops))
        self.assertEqual({0: 1, 3: 1, 5: 3, 7: 2}, p.pops)

    def test_trackPop_inputData_80(self):
        p1 = lanternfish.popTracker(initialTimer=0)
        result = p1.trackPop(self.initialTimers, 80)
        self.assertEqual(386536, result)

    def test_trackPop_inputData_256(self):
        p2 = lanternfish.popTracker(initialTimer=0)
        result = p2.trackPop(self.initialTimers, 256)
        self.assertEqual(1732821262171, result)

    def test_trackPop_testData_18(self):
        p = lanternfish.popTracker(initialTimer=0)
        result = p.trackPop([3, 4, 3, 1, 2], 18)
        self.assertEqual(26, result)

    def test_trackPop_testData_80(self):
        p = lanternfish.popTracker(initialTimer=0)
        result = p.trackPop([3, 4, 3, 1, 2], 80)
        self.assertEqual(5934, result)

    def test_trackPop_testData_256(self):
        p = lanternfish.popTracker(initialTimer=0)
        result = p.trackPop([3, 4, 3, 1, 2], 256)
        self.assertEqual(26984457539, result)

    def test_bruteForce_count_testData_18(self):
        p = lanternfish.popTracker()
        result = p.bruteForceSolution([3, 4, 3, 1, 2], 18)
        self.assertEqual(26, result)

    def test_bruteForce_count_testData_80(self):
        p = lanternfish.popTracker()
        result = p.bruteForceSolution([3, 4, 3, 1, 2], 80)
        self.assertEqual(5934, result)

    def test_bruteForce_population_testData_18(self):
        """
        Check that the brute force solution matches the timers detailed in the spec.
        """
        p = lanternfish.popTracker()
        result = p.bruteForceSolution([3, 4, 3, 1, 2], 18)
        expectedTimers = [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]
        uniqueTimers = set(expectedTimers)
        expectedCollated = {t: expectedTimers.count(t) for t in uniqueTimers}
        # {0: 3, 1: 5, 2: 3, 3: 2, 4: 2, 5: 1, 6: 5, 7: 1, 8: 4}
        self.assertEqual(expectedCollated, p.pops)

    def test_bruteForce_count_inputData_80(self):
        p = lanternfish.popTracker()
        result = p.bruteForceSolution(self.initialTimers, 80)
        self.assertEqual(386536, result)

    def test_bruteForce_count_inputData_256(self):
        p = lanternfish.popTracker()
        result = p.bruteForceSolution(self.initialTimers, 256)
        self.assertEqual(1732821262171, result)

if __name__ == '__main__':
    unittest.main()
