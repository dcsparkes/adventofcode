"""
https://adventofcode.com/2020/day/13
"""
from base import base
import math
import unittest


class MyTestCase(unittest.TestCase):
    fInput1 = "input2020_13a.txt"
    fTest1a = "test2020_13a.txt"
    fTest1b = "test2020_13b.txt"
    fTest1c = "test2020_13c.txt"
    fTest1d = "test2020_13d.txt"
    fTest1e = "test2020_13e.txt"
    fTest1f = "test2020_13f.txt"

    def test_firstTimestamp_fInput1(self):
        result = findTimestamp(self.fInput1)
        print("Part 2: {}".format(result))
        self.assertEqual(534035653563227, result)

    def test_firstTimestamp_fTest1a(self):
        self.assertEqual(1068781, findTimestamp(self.fTest1a))

    def test_firstTimestamp_fTest1b(self):
        self.assertEqual(3417, findTimestamp(self.fTest1b))

    def test_firstTimestamp_fTest1c(self):
        self.assertEqual(754018, findTimestamp(self.fTest1c))

    def test_firstTimestamp_fTest1d(self):
        self.assertEqual(779210, findTimestamp(self.fTest1d))

    def test_firstTimestamp_fTest1e(self):
        self.assertEqual(1261476, findTimestamp(self.fTest1e))

    def test_firstTimestamp_fTest1f(self):
        self.assertEqual(1202161486, findTimestamp(self.fTest1f))

    def test_nextBus_Input1(self):
        result = nextBus(self.fInput1)[0]
        print("Part 1: {}".format(result))
        self.assertEqual(2165, result)

    def test_nextBus_fTest1(self):
        self.assertEqual(295, nextBus(self.fTest1a)[0])


def chineseRemainderSolution(modulos):
    """
    https://mathworld.wolfram.com/ChineseRemainderTheorem.html
    https://en.wikipedia.org/wiki/Chinese_remainder_theorem

    :param modulos: list of tuples
    :return:
    """
    pass


def nextBus(fileName):
    shortestWait = float('inf')
    idNearest = None
    timestamp = None
    for stamp in base.getInputLines(fileName, delimiter=','):
        if stamp == 'x':
            pass
        elif timestamp:
            delay = timestamp % int(stamp)
            if delay < shortestWait:
                shortestWait = delay
                idNearest = int(stamp)
        else:
            timestamp = -int(stamp)
    return (shortestWait * idNearest, shortestWait, idNearest)


def findTimestamp(fileName):
    ids = readIDs(fileName)
    buses = list(zip(*ids))[0]
    candidate = ids[0][0] - ids[0][1]
    increment = ids[0][0]

    for bus, offset in ids[1:]:
        while -candidate % bus != offset % bus:
            oldOffset = -candidate % bus
            candidate += increment
            newOffset = -candidate % bus
        increment = math.lcm(increment, bus)
    return candidate


def readIDs(fileName):
    firstIgnored = False
    ids = []
    offset = 0
    for stamp in base.getInputLines(fileName, delimiter=','):
        if not firstIgnored:
            firstIgnored = True
        elif stamp == 'x':
            offset += 1
        else:
            ids.append((int(stamp), offset))
            offset += 1
    return ids


if __name__ == '__main__':
    unittest.main()
