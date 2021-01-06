"""
https://adventofcode.com/2017/day/4
"""
from base import base


def countLinesWithoutAnagrams(fileName):
    count = 0
    for line in base.getInputLines(fileName):
        sortedWords = [''.join(sorted(w)) for w in line.split(' ')]
        if len(sortedWords) == len(set(sortedWords)):
            count += 1
    return count


def countLinesWithoutDuplicates(fileName):
    count = 0
    for line in base.getInputLines(fileName):
        splitLine = line.split(' ')
        if len(splitLine) == len(set(splitLine)):
            count += 1
    return count


if __name__ == '__main__':
    print("Part 1: {}".format(countLinesWithoutDuplicates("input2017_04a.txt")))
    print("Part 2: {}".format(countLinesWithoutAnagrams("input2017_04a.txt")))
