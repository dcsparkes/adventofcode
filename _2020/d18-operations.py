"""
https://adventofcode.com/2020/day/18
"""
import inspect
import logging
import re
import unittest
from base import base

logging.basicConfig(filename='../log/{}.log'.format(__name__), level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def evaluateUnparenthesisedAddthenMultiply(statement):
    logger.debug("{}: statement=\"{}\"".format(inspect.currentframe().f_code.co_name, statement))

    if '(' in statement or ')' in statement:
        raise SyntaxError("\"{}\" contains parentheses.".format(statement))

    matchString = r"(.*?)(\d+ \+ \d+)(.*)"
    partiallyParsed = statement
    match = re.match(matchString, statement)
    while match:
        logger.debug("{}: match=\"{}\"\n{}".format(inspect.currentframe().f_code.co_name, match, '\n'.join(
            ["match.group({}): {}".format(i, match.group(i)) for i in range(1, 4)])))
        partiallyParsed = ''.join([match.group(1), str(eval(match.group(2))), match.group(3)])
        logger.debug("{}: partiallyParsed=\"{}\"".format(inspect.currentframe().f_code.co_name, partiallyParsed))
        match = re.match(matchString, partiallyParsed)

    retVal = str(eval(partiallyParsed))
    logger.debug("{}: Return Value=\"{}\"".format(inspect.currentframe().f_code.co_name, retVal))
    return retVal


def evaluateUnparenthesisedLefttoRight(statement):
    if '(' in statement or ')' in statement:
        raise SyntaxError("\"{}\" contains parentheses.".format(statement))

    partiallyParsed = statement
    matchString = r"(\d+ . \d+)(.*)"
    match = re.match(matchString, statement)
    while match:
        partiallyParsed = ''.join([str(eval(match.group(1))), match.group(2)])
        match = re.match(matchString, partiallyParsed)
    return partiallyParsed


def parse(statement, evalFunc=evaluateUnparenthesisedLefttoRight):
    logger.debug("{}: statement=\"{}\"".format(inspect.currentframe().f_code.co_name, statement))

    matchString = r"(.*)(\(.*?\))(.*)$"
    partiallyParsed = statement
    match = re.match(matchString, statement)
    while match:
        partiallyParsed = ''.join(
            [str(match.group(1)), evalFunc(match.group(2).strip('()')), match.group(3)])
        logger.debug("{}: partiallyParsed=\"{}\"".format(inspect.currentframe().f_code.co_name, partiallyParsed))
        match = re.match(matchString, partiallyParsed)

    retVal = evalFunc(partiallyParsed)
    logger.debug("{}: Return Value=\"{}\"".format(inspect.currentframe().f_code.co_name, retVal))
    return retVal


def parseFile(fileName, evalFunc=evaluateUnparenthesisedLefttoRight):
    total = 0
    for line in base.getInputLines(fileName):
        total += int(parse(line, evalFunc))
    return total


class TestParse(unittest.TestCase):
    fInput1a = "input2020_18a.txt"

    knownAnswers1 = ("1 + 2 * 3 + 4 * 5 + 6", 71)
    knownAnswers2 = ("1 + (2 * 3) + (4 * (5 + 6))", 51)
    knownAnswers3 = ("2 * 3 + (4 * 5)", 26)
    knownAnswers4 = ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437)
    knownAnswers5 = ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240)
    knownAnswers6 = ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632)
    knownAnswers7 = ("1 * 12 + 13 * 1", 25)

    def test_parseFile_AddthenMultiply_unknownAnswers1(self):
        answer = parseFile(self.fInput1a, evaluateUnparenthesisedAddthenMultiply)
        print("Part2: {}".format(answer))
        self.assertEqual(351175492232654, answer)

    def test_parseFile_LtoR_unknownAnswers1(self):
        answer = parseFile(self.fInput1a)
        print("Part1: {}".format(answer))
        self.assertEqual(16332191652452, answer)

    def test_parse_AddthenMultiply_knownAnswers1(self):
        statement, expected = self.knownAnswers1
        expected = "231"
        self.assertEqual(str(expected), parse(statement, evaluateUnparenthesisedAddthenMultiply))

    def test_parse_AddthenMultiply_knownAnswers2(self):
        statement, expected = self.knownAnswers2
        self.assertEqual(str(expected), parse(statement, evaluateUnparenthesisedAddthenMultiply))

    def test_parse_AddthenMultiply_knownAnswers3(self):
        statement, expected = self.knownAnswers3
        expected = "46"
        self.assertEqual(str(expected), parse(statement, evaluateUnparenthesisedAddthenMultiply))

    def test_parse_AddthenMultiply_knownAnswers4(self):
        statement, expected = self.knownAnswers4
        expected = "1445"
        self.assertEqual(str(expected), parse(statement, evaluateUnparenthesisedAddthenMultiply))

    def test_parse_AddthenMultiply_knownAnswers5(self):
        statement, expected = self.knownAnswers5
        expected = "669060"
        self.assertEqual(str(expected), parse(statement, evaluateUnparenthesisedAddthenMultiply))

    def test_parse_AddthenMultiply_knownAnswers6(self):
        statement, expected = self.knownAnswers6
        expected = "23340"
        # print("LOGGER LEVEL = {}".format(logger.level))
        oldLoggerLevel = logger.level
        logger.setLevel("DEBUG")
        self.assertEqual(str(expected), parse(statement, evaluateUnparenthesisedAddthenMultiply))
        logger.setLevel(oldLoggerLevel)

    def test_parse_AddthenMultiply_knownAnswers7(self):
        statement, expected = self.knownAnswers7
        # expected = "669060"
        self.assertEqual(str(expected), parse(statement, evaluateUnparenthesisedAddthenMultiply))

    def test_parse_LtoR_knownAnswers1(self):
        statement, expected = self.knownAnswers1
        self.assertEqual(str(expected), parse(statement))

    def test_parse_LtoR_knownAnswers2(self):
        statement, expected = self.knownAnswers2
        self.assertEqual(str(expected), parse(statement))

    def test_parse_LtoR_knownAnswers3(self):
        statement, expected = self.knownAnswers3
        self.assertEqual(str(expected), parse(statement))

    def test_parse_LtoR_knownAnswers4(self):
        statement, expected = self.knownAnswers4
        self.assertEqual(str(expected), parse(statement))

    def test_parse_LtoR_knownAnswers5(self):
        statement, expected = self.knownAnswers5
        self.assertEqual(str(expected), parse(statement))

    def test_parse_LtoR_knownAnswers6(self):
        statement, expected = self.knownAnswers6
        self.assertEqual(str(expected), parse(statement))

    def test_parse_LtoR_knownAnswers7(self):
        statement, expected = self.knownAnswers7
        self.assertEqual(str(expected), parse(statement))

    def test_evaluateUnparenthesisedAddthenMultiply_knownAnswers1(self):
        statement, expected = self.knownAnswers1
        expected = "231"
        self.assertEqual(expected, evaluateUnparenthesisedAddthenMultiply(statement))

    def test_evaluateUnparenthesisedAddthenMultiply_parentheses(self):
        self.assertRaises(SyntaxError, evaluateUnparenthesisedAddthenMultiply, self.knownAnswers3[0])

    def test_evaluateUnparenthesisedLefttoRight_knownAnswers1(self):
        statement, expected = self.knownAnswers1
        self.assertEqual(str(expected), evaluateUnparenthesisedLefttoRight(statement))

    def test_evaluateUnparenthesisedLefttoRight_parentheses(self):
        self.assertRaises(SyntaxError, evaluateUnparenthesisedLefttoRight, self.knownAnswers3[0])


if __name__ == '__main__':
    unittest.main()
    # statement = "1 + 2 * 3 + 4 * 5 + 6"
    parse(statement)
