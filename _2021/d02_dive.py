"""
https://adventofcode.com/2021/day/2
"""
from base import base

import logging
import sys


def readVectors(fileName):
    for instruction in base.getInputLines(fileName):
        direction, distance = instruction.split()

        unitVectors = {"forward": (1, 0),
                       "up": (0, -1),
                       "down": (0, 1),
                       }

        vector = tuple([x * int(distance) for x in unitVectors[direction]])
        logging.debug("{}(\"{}\"): direction: \"{}\", distance: {}, vector: {}".format(sys._getframe().f_code.co_name,
                                                                                       instruction, direction, distance,
                                                                                       vector))
        yield vector


def readVectorsV2(fileName):
    aim = [1, 0]
    for instruction in base.getInputLines(fileName):
        direction, distString = instruction.split()

        distance = int(distString)
        if direction == "down":
            aim[1] += distance
        elif direction == "up":
            aim[1] -= distance
        elif direction == "forward":
            moveVector = tuple([x * distance for x in aim])
            yield moveVector
        else:
            logging.warning("{}(\"{}\"): Unrecognised direction: \"{}\"".format(sys._getframe().f_code.co_name,
                                                                                fileName, direction))


def addVectors(a, b):
    """
    Add two vector tuples.

    :param a: vector a
    :param b: vector b
    :return: a + b
    """
    result = tuple([sum(x) for x in zip(a, b)])
    logging.debug("{}({}, {}): result: {}".format(sys._getframe().f_code.co_name,
                                                  a, b, result))

    return result


def calcFinalPosition(fileName, readFunc=readVectors):
    position = (0, 0)
    for move in readFunc(fileName):
        position = addVectors(position, move)
    return position


def calculateSweptRectangle(fileName, title, readFunc=readVectors):
    position = calcFinalPosition(fileName, readFunc)
    sweptRectangleArea = position[0] * position[1]
    print("{}: End: {}, Area: {}".format(title, position, sweptRectangleArea))


if __name__ == '__main__':
    logging.basicConfig(filename="../log/2021_d02.log", encoding='utf-8', level=logging.INFO)
    calculateSweptRectangle("../input/test2021_02a.txt", "Task 1: Test 02a")
    calculateSweptRectangle("../input/input2021_02a.txt", "Task 1: Input 02a")
    calculateSweptRectangle("../input/test2021_02a.txt", "Task 2: Test 02a", readVectorsV2)
    calculateSweptRectangle("../input/input2021_02a.txt", "Task 2: Input 02a", readVectorsV2)
