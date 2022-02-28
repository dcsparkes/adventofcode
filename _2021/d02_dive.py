"""
https://adventofcode.com/2021/day/2
"""
from base import base

import logging
import sys


def readInstructions(fileName):
    """

    :param fileName:
    :return:
    """
    for line in base.getInputLines(fileName):
        yield line


def convertInstructionToVector(instruction):
    direction, distance = instruction.split()

    unitVectors = {"forward": (1, 0),
                   "up": (0, -1),
                   "down": (0, 1),
                   }

    vector = tuple([x * int(distance) for x in unitVectors[direction]])
    logging.debug("{}(\"{}\"): direction: \"{}\", distance: {}, vector: {}".format(sys._getframe().f_code.co_name,
                                                                       instruction, direction, distance, vector))
    return vector


def readVectors(fileName):
    for instruction in readInstructions(fileName):
        yield convertInstructionToVector(instruction)


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

def calcFinalPosition(fileName):
    position = (0, 0)
    for move in readVectors(fileName):
        position = addVectors(position, move)
    return position

def calculateSweptRectangle(fileName, title):
    position = calcFinalPosition(fileName)
    sweptRectangleArea = position[0] * position[1]
    print("{}: End: {}, Area: {}".format(title, position, sweptRectangleArea))


if __name__ == '__main__':
    logging.basicConfig(filename="../log/2021_d02.log", encoding='utf-8', level=logging.DEBUG)
    calculateSweptRectangle("../input/test2021_02a.txt", "Test 02a")
    calculateSweptRectangle("../input/input2021_02a.txt", "Input 02a")
