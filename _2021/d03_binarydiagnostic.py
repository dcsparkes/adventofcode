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
    orderedcounts = [sorted(d.items(), key=lambda x: x[1]) for d in counts]
    # print(orderedcounts)
    losers = ''.join([d[0][0] for d in orderedcounts])
    winners = ''.join([d[-1][0] for d in orderedcounts])
    return (winners, losers)


def powerConsumption(fileName):
    winners, losers = parseCounts(fileName)
    gamma = int(winners, 2)
    epsilon = int(losers, 2)
    return ("gamma: {}, epsilon: {}, product: {}".format(gamma, epsilon, gamma * epsilon))


LOW, BOTH, HIGH = range(-1, 2)


def splitLists(binaries, select=BOTH):
    """
    Recursive select either the most frequent digit at each position or the least frequent or both (root of tree).

    :param binaries: list of binary strings
    :param select: Selection criteria
    :return: Strings tuple (winners, [losers])
    """
    retVal = None
    logging.debug("{}({}, select={})".format(sys._getframe().f_code.co_name, binaries, select))

    returnStrings = []
    sortStore = {}
    if len(binaries) == 0:  # If there are no strings then the empty string is appropriate
        if select == BOTH:
            retVal = ("", "")
        else:
            retVal = ("",)
    elif len(binaries) == 1:  # If there is only one string then the string is both the most and least frequent.
        if select == BOTH:
            retVal = (binaries[0], binaries[0])
        else:
            retVal = (binaries[0],)
    else:
        for bString in binaries:
            prefix = bString[0]
            suffix = bString[1:]
            if prefix not in sortStore:
                sortStore[prefix] = [suffix]
            else:
                sortStore[prefix].append(suffix)

        counts = sorted([(len(sortStore[k]), k) for k in sortStore.keys()])
        if select == LOW or select == BOTH:
            prefix = counts[0][1]
            returnStrings.append(prefix + splitLists(sortStore[prefix], select=LOW)[0])

        if select == HIGH or select == BOTH:
            prefix = counts[-1][1]
            returnStrings.append(prefix + splitLists(sortStore[prefix], select=HIGH)[0])
        retVal = tuple(returnStrings)

    logging.debug("{}({}, select={}), return=\"{}\"".format(sys._getframe().f_code.co_name, binaries, select, retVal))
    return retVal


def lifeSupportRating(fileName):
    readings = list(base.getInputLines(fileName))
    oxygenGeneratorRating, co2ScrubberRating = splitLists(readings)
    o2rating = int(oxygenGeneratorRating, 2)
    co2rating = int(co2ScrubberRating, 2)
    return "O2: {} ({}), CO2: {} ({}), Rating: {}".format(oxygenGeneratorRating, o2rating, co2ScrubberRating, co2rating,
                                                          o2rating * co2rating)


if __name__ == '__main__':
    logging.basicConfig(filename="../log/2021_d03.log", encoding='utf-8', level=logging.WARNING)
    print("Test:  " + powerConsumption("../input/test2021_03a.txt"))
    print("Input: " + powerConsumption("../input/input2021_03a.txt"))
    print("Test:  " + lifeSupportRating("../input/test2021_03a.txt"))
    print("Input: " + lifeSupportRating("../input/input2021_03a.txt"))
