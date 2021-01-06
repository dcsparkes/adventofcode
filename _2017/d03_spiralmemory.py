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
    sideLen = 2 * ringID
    sidePos = (num - bottomRange) % sideLen
    midPoint = ringID
    sideDist = abs(sidePos - midPoint)
    return ringID + sideDist


def coordSequence():
    x_move = 1
    y_move = -1
    xPos = 0
    yPos = 0
    moveCount = 1
    while True:
        for _ in range(moveCount):
            yield xPos, yPos
            xPos += x_move
        x_move = -x_move
        for _ in range(moveCount):
            yield xPos, yPos
            yPos += y_move
        y_move = -y_move
        moveCount += 1


def neighbourCoords(x, y):
    for m in range(x - 1, x + 2):
        for n in range(y - 1, y + 2):
            yield m, n


def spiralValues():
    calculated = set([(0, 0)])
    valueDict = {(0, 0): 1}
    for coord in coordSequence():
        value = valueDict[coord]
        calculated.add(coord)
        yield value
        for n in neighbourCoords(*coord):
            if n not in calculated:
                if n in valueDict:
                    valueDict[n] += value
                else:
                    valueDict[n] = value


if __name__ == '__main__':
    print("Part 1: {}".format(spiralDistance(368078)))
    for val in spiralValues():
        if val > 368078:
            print("Part 2: {}".format(val))
            break
