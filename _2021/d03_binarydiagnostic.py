"""
https://adventofcode.com/2021/day/3
"""
from base import base

import logging
import sys


def countDigits(fileName):
    """
    Count the digits in each position of a set of numbers.  Do not assume same lengths or exclusive membership of a
    digit set.

    :param fileName: Input file
    :return: (total count of numbers, [counts of each digit])
    """
    counts = []

    for digits in base.getInputLines(fileName):
        # print("\"{}\", len:{}".format(digits, len(digits)))
        shortfall = len(digits) - len(counts)
        counts.extend([dict() for i in range(shortfall)])
        for i in range(len(digits)):
            if digits[i] in counts[i]:
                counts[i][digits[i]] += 1
            else:
                counts[i][digits[i]] = 1
    return counts


def parseCounts(fileName):
    """
    Return number strings contaning the most popular digits and the least popular.

    :param fileName: File containing list of digit strings
    :return: Tuple of number strings containing the most popular digits and the least popular.
    """
    counts = countDigits(fileName)
    # print(counts)
    orderedcounts = [sorted(d.items(), key=lambda x:x[1]) for d in counts]
    # print(orderedcounts)
    losers = ''.join([d[0][0] for d in orderedcounts])
    winners = ''.join([d[-1][0] for d in orderedcounts])
    return (winners, losers)

def powerConsumption(fileName):
    winners, losers = parseCounts(fileName)
    gamma = int(winners, 2)
    epsilon = int(losers, 2)
    return("gamma: {}, epsilon: {}, product: {}".format(gamma, epsilon, gamma * epsilon))


if __name__ == '__main__':
    logging.basicConfig(filename="../log/2021_d03.log", encoding='utf-8', level=logging.INFO)
    print("Test:  " + powerConsumption("../input/test2021_03a.txt"))
    print("Input: " + powerConsumption("../input/input2021_03a.txt"))
