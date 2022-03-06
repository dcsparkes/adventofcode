"""
https://adventofcode.com/2021/day/5
"""

# import logging
# import sys
import re

from base import base
from cartesian import lines


def readLines(fileName, ignoreDiagonals=False):
    pattern = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
    for line in base.getInputLines(fileName):
        match = pattern.match(line)
        if match:
            x1, y1, x2, y2 = match.groups()
            if not ignoreDiagonals or x1 == x2 or y1 == y2:
                yield lines.Line((x1, y1), (x2, y2))


def calculateIntersections(fileName, ignoreDiagonals=False):
    intersections = {}
    for line in readLines(fileName, ignoreDiagonals):
        for point in line.points():
            if point in intersections:
                intersections[point] += 1
            else:
                intersections[point] = 1
    return intersections


if __name__ == '__main__':
    # logging.basicConfig(filename="../log/2021_d05.log", encoding='utf-8', level=logging.WARNING)
    fInput = "input2021_05a.txt"
    fTest = "test2021_05a.txt"

    intersectsOrthogonal = calculateIntersections(fInput, ignoreDiagonals=True)
    print(len([x for x in intersectsOrthogonal.values() if x > 1]))

    intersects = calculateIntersections(fInput)
    print(len([x for x in intersects.values() if x > 1]))