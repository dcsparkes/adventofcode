"""
https://adventofcode.com/2016/day/6
"""
from base import base


class RepetitionDecoder:
    def __init__(self, fileName=None):
        self.repetitions = []
        if fileName:
            self.readRepetitions(fileName)

    def readRepetitions(self, fileName):
        for line in base.getInputLines(fileName):
            self.repetitions.append(line.strip())

    def decode(self, mostFrequent=True):
        message = []
        for column in zip(*self.repetitions):
            if mostFrequent:
                message.append(self.findFrequencies(column)[-1])
            else:
                message.append(self.findFrequencies(column)[0])
        return ''.join(message)

    def findMostFrequent(self, text):
        text = sorted(text)
        maxCount = 0
        maxChar = None
        while text:
            char = text[-1]
            count = text.count(char)
            if count > maxCount:
                maxCount = count
                maxChar = char
            text = text[:-count]
        return maxChar

    def findFrequencies(self, text):
        text = sorted(text)
        counts = {}
        while text:
            char = text[-1]
            count = text.count(char)
            counts[char] = count
            text = text[:-count]
        return [k for k in sorted(counts, key=counts.get)]



if __name__ == '__main__':
    # rd = RepetitionDecoder("test2016_06a.txt")
    rd = RepetitionDecoder("input2016_06a.txt")
    print("Part 1: '{}'".format(rd.decode()))
    print("Part 2: '{}'".format(rd.decode(mostFrequent=False)))
