"""
https://adventofcode.com/2015/day/8
"""
import inspect
import logging
import re
import unittest
from base import base
from stringprocessor import stringprocessor

logging.basicConfig(filename='../log/{}.log'.format(__name__), level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


def regexMatch(matchString, source):
    logger.debug(
        "{}: matchString = <{}>: source = <{}>".format(inspect.currentframe().f_code.co_name, matchString, source))
    match = re.match(matchString, source)
    if match:
        for i in range(1, 9):
            # print("{}: {}".format(i, match.group(i)))
            logger.debug(
                "{}: matchString = <{}>: source = <{}>: yielding <{}>".format(inspect.currentframe().f_code.co_name,
                                                                              matchString, source, match.group(i)))
            yield match.group(i)


def countMemChars(line):
    startLength = len(line)
    matchString = r"\"(.*)\""
    logger.debug(
        "{}: partiallyResolvedLine=\"{}\": len = {}".format(inspect.currentframe().f_code.co_name, line, len(line)))
    matches = regexMatch(matchString, line)

    partiallyResolvedLine = next(matches).replace(r"\\", "H").replace(r"\"", "W")
    logger.debug(
        "{}: partiallyResolvedLine=\"{}\"".format(inspect.currentframe().f_code.co_name, partiallyResolvedLine))

    matchString = r"(.*)([\\]x[0-9a-f]{2})(.*)"
    match = re.match(matchString, partiallyResolvedLine)
    logger.debug(
        "{}: partiallyResolvedLine=\"{}\"".format(inspect.currentframe().f_code.co_name, partiallyResolvedLine))
    if match:
        partiallyResolvedLine = 'X'.join([match.group(1), match.group(3)])
        logger.debug(
            "{}: partiallyResolvedLine=\"{}\"".format(inspect.currentframe().f_code.co_name, partiallyResolvedLine))

    length = len(partiallyResolvedLine)
    print("Original: <{}>. Current <{}>. Diff: <{}>".format(line, partiallyResolvedLine, startLength - length))
    return startLength - length


def decodeFile(fileName):
    total = 0
    length = 0
    sp = stringprocessor.StringEncoder()
    for line in base.getInputLines(fileName):
        processed = sp.processLine(line)
        print("Original: <{}>. Current <{}>. Diff: {} - {} = {}".format(line, processed, len(line), len(processed),
                                                                        len(line) - len(processed)))
        total -= len(line) - len(processed)
    return total


def parseFile(fileName):
    total = 0
    length = 0
    sp = stringprocessor.StringDecoder()
    for line in base.getInputLines(fileName):
        processed = sp.processLine(line)
        print("Original: <{}>. Current <{}>. Diff: {} - {} = {}".format(line, processed, len(line), len(processed),
                                                                        len(line) - len(processed)))
        total += len(line) - len(processed)
    return total


class TestMatchsticks(unittest.TestCase):
    fInput1a = "input2015_08a.txt"
    fTest1a = "test2015_08a.txt"
    fTest1b = "test2015_08b.txt"

    def test_countMemChars_Ascii(self):
        self.assertEqual(12, parseFile(self.fTest1a))

    def test_parseFile_fTest1a(self):
        self.assertEqual(12, parseFile(self.fTest1a))

    def test_parseFile_fTest1b(self):
        self.assertEqual(24 - 10, parseFile(self.fTest1b))

    def test_parseFile_fInput1a(self):
        self.assertEqual(1350, parseFile(self.fInput1a))

    def test_decodeFile_fInput1a(self):
        self.assertEqual(2085, decodeFile(self.fInput1a))


if __name__ == '__main__':
    unittest.main()
