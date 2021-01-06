"""
https://adventofcode.com/2017/day/3
"""
import math


def identifyRingIterative(num):
    i = 1
    ringID = 0
    while i ** 2 < num:
        i += 2
        ringID += 1
    return ringID


def identifyRingMathematical(num):
    root = math.sqrt(num)
    roundedUp = root + (-root % 1)
    return int((roundedUp) / 2)


identifyRing = identifyRingMathematical


def spiralDistance(num):
    ringID = identifyRing(num)
    if not ringID:
        return 0
    bottomRange = (2 * ringID - 1) ** 2
    topRange = (2 * ringID + 1) ** 2
    sideLen = (topRange - bottomRange) // 4
    sidePos = (num - bottomRange) % sideLen
    midPoint = sideLen // 2
    sideDist = abs(sidePos - midPoint)
    print("num: {}, ringID: {}, bottomRange: {}, topRange: {}, sideLen: {}, sidePos: {}, midPoint: {}, sideDist: {}".format(
        num, ringID, bottomRange, topRange, sideLen, sidePos, midPoint, sideDist))
    return ringID + sideDist

if __name__ == '__main__':
    print("Part 1: {}".format(spiralDistance(368078)))

