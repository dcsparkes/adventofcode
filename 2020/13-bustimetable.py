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
        self.assertEqual(534035653563227, findTimestamp(self.fInput1))

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
        self.assertEqual(2165, nextBus(self.fInput1)[0])

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
        # print("{}:{}".format(stamp, type(stamp)))
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
    print("findTimestamp: {} : {}: {}: {}".format(ids, type(ids), type(ids[0]), type(ids[0][0])))
    candidate = ids[0][0] - ids[0][1]
    increment = ids[0][0]

    for bus, offset in ids[1:]:
        # print("{0:<13}:".format(increment), ids)
        # print("{0:<13}: ".format(candidate), end = '')
        # print([(bus, -candidate % bus) for bus in buses])

        while -candidate % bus != offset % bus:
            oldOffset = -candidate % bus
            candidate += increment
            newOffset = -candidate % bus
            # print("candidate: {} = {} * {} + {} : {}".format(candidate, bus,  candidate//bus,
            #                                                  candidate % bus, -candidate % bus))
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
    # print(ids)
    return ids


if __name__ == '__main__':
    # unittest.main()
    # (ans, a, b) = nextBus("input2020_13a.txt")
    # print(ans)
    print(findTimestamp("test2020_13c.txt"))
    # print(findTimestamp("input2020_13a.txt"))


