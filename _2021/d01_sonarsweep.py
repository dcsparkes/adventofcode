"""
https://adventofcode.com/2021/day/1
"""
from base import base

def rollingSum(fileName, windowSize=3):
    """
    Generate a rolling sum of windowsize integers.
    :param fileName:
    :param windowSize:
    :return:
    """
    window = []
    for depth in base.getInts(fileName):
        window.append(depth)

        if len(window) >= windowSize:
            window = window[-windowSize:]
            yield sum(window)


def countDepthIncreases(fileName, windowSize=1):
    """

    :param fileName:
    :return:
    """
    prev = None
    count = 0

    for depth in rollingSum(fileName, windowSize):
        if prev is not None:
            if depth > prev:
                count += 1
        prev = depth
    return count

if __name__ == '__main__':
    print(countDepthIncreases("../input/test2021_01a.txt"))  # Should be 7
    print(countDepthIncreases("../input/input2021_01a.txt"))  # Answer to part a: 1696
    print(countDepthIncreases("../input/test2021_01a.txt", 3))  # Should be 5
    print(countDepthIncreases("../input/input2021_01a.txt", 3))  # Answer to part b: 1737
