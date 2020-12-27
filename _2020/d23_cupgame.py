"""
https://adventofcode.com/2020/day/23
"""
from indexedlinkedlist import indexedlinkedlist


def decrementModular(value, size):
    returnValue = (value - 1) % size
    if not returnValue:
        returnValue += size
    return returnValue


def move(circle):
    claw = circle.popSlice(1, 4)
    selection = decrementModular(circle[0], circle.size)  # circle.size or length?
    while selection in claw:
        selection = decrementModular(selection, circle.size)
    circle.insertAfterValue(selection, claw)
    circle.rotate()


def playGame(input, iterations, fullReport=True, size=None):
    circle = indexedlinkedlist.IndexedList(input, size)

    for i in range(iterations):
        move(circle)

    return report(circle, fullReport)


def playTenMillion(input):
    # Pad input to a million numbers - 1000000
    return playGame(input, iterations=10000000, fullReport=False, size=1000000)


def report(iList, full=True):
    iList.rotateToOne()
    if full:
        return [i for i in iList if i != 1]
    else:
        return iList[1] * iList[2]


if __name__ == '__main__':
    pass
