"""
https://adventofcode.com/2020/day/16
"""
import inspect
import logging
import math
import re
import unittest
from base import base

logging.basicConfig(filename='../log/{}.log'.format(__name__), level=logging.DEBUG)
logger = logging.getLogger(__name__)

ST_INITIAL, ST_YOUR_TICKET, ST_NEARBY_TICKETS = range(1, 4)


class TicketRule:
    def __init__(self, *args, name=""):
        self.name = name.strip(' ')
        self.ranges = self._pairwiseGroup(*args)

    # def __eq__(self, other):
    #     return self.name == other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __le__(self, other):
        return self.name <= other.name

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return "{}(name={})".format(self.__class__.__name__, self.name)

    def __str__(self):
        return self.name

    @staticmethod
    def _pairwiseGroup(*args):
        integers = [int(num) for num in args]
        pairs = []
        for i in range(0, len(args), 2):
            pairs.append(tuple(integers[i:i + 2]))
        return pairs

    def validate(self, value):
        for pair in self.ranges:
            if pair[0] <= value <= pair[1]:
                return True
        return False


class TicketValidator:
    def __init__(self, fileName=None):
        # self.rangesAcceptable = []
        self.rules = []
        self.state = None
        self.invalidValueSum = 0
        self.myTicket = None
        self.tickets = []
        self.columnHeaders = []

    def _isValid(self, value):
        for rule in self.rules:
            if rule.validate(value):
                return True
        return False

    def identifyCandidates(self):
        # print(self.tickets)
        columns = zip(*self.tickets)
        # print(columns)
        headerCandidates = []
        for col in columns:
            candidates = []
            # print("Start of rule loop: {}:{}".format(col, candidates))
            for rule in self.rules:
                candidatePossible = True
                # print("Start of val loop: \"{}\":{}".format(rule, candidatePossible))
                for val in col:
                    candidatePossible &= rule.validate(val)
                # print("End of val loop: \"{}\":{}".format(rule, candidatePossible))
                if candidatePossible:
                    candidates.append(rule)
            # print("End of rule loop: {}:{}".format(col, candidates))
            headerCandidates.append(candidates)

        return headerCandidates

    def generateColumnHeaders(self):
        """
        Identify unique rules for columns OR unique columns for rules.
        :return:
        """
        candidatesPerColumn = self.identifyCandidates()
        logger.debug("{}.{}: {} candidates:\n{}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, len(candidatesPerColumn),
            '\n'.join([str(cs) for cs in candidatesPerColumn])))
        self.whittleByColumn(candidatesPerColumn)
        logger.debug("{}.{}: {} whittled candidates:\n{}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, len(candidatesPerColumn),
            '\n'.join([str(cs) for cs in candidatesPerColumn])))

        if max([len(cs) for cs in candidatesPerColumn]) > 1:
            logger.critical("{}.{}: Multiple candidates: {}.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, candidatesPerColumn))
        if min([len(cs) for cs in candidatesPerColumn]) < 1:
            logger.critical("{}.{}: Empty candidates: {}.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, candidatesPerColumn))
        self.columnHeaders = [h[0] for h in candidatesPerColumn]

    def whittleByColumn(self, candidates):
        # lengths = sorted([(len(candidates[i]), i) for i in range(len(candidates))])
        # for length, index in lengths:
        #     if len(candidates[index]) == 1:
        #         rule = candidates[index][0]
        #         for j in range(len(candidates)):
        #             if j != index and rule in candidates[j]:
        #                 candidates[j].remove(rule)
        candidateCopy = sorted(candidates[:], key=len)  # list copied, but the member lists 'passed' by reference.
        for i in range(len(candidateCopy)):
            if len(candidateCopy[i]) == 1:
                rule = candidateCopy[i][0]
                for j in range(i + 1, len(candidateCopy)):
                    candidateCopy[j].remove(rule)

    def calculateDepartureMultiple(self):
        if not self.columnHeaders:
            self.generateColumnHeaders()

        departures = [b for a, b in zip(self.columnHeaders, self.myTicket) if str(a)[:9] == "departure"]
        # print(departures)
        # print(math.prod(departures))

        return math.prod(departures)

    def printMyTicket(self):
        if not self.columnHeaders:
            self.generateColumnHeaders()

        pairs = sorted(list(zip(self.columnHeaders, self.myTicket)))
        return ', '.join([': '.join([str(a), str(b)]) for a, b in pairs])

    def readInput(self, fileName):
        self.state = ST_INITIAL

        for line in base.getInputLines(fileName):
            # print("{}: {}".format(self.state, line))
            if not line:
                pass
            elif line[:12] == "your ticket:":
                msg = '\n'.join(["{}: {}".format(rule.name, rule.ranges) for rule in self.rules])
                logger.debug("{}.{}: STATE CHANGE => ST_YOUR_TICKET: {} rules:\n{}".format(
                    self.__class__.__name__, inspect.currentframe().f_code.co_name, len(self.rules), msg))
                self.state = ST_YOUR_TICKET
            elif line == "nearby tickets:":
                logger.debug("{}.{}: STATE CHANGE => ST_NEARBY_TICKETS: My ticket: {}".format(
                    self.__class__.__name__, inspect.currentframe().f_code.co_name, self.myTicket))
                self.state = ST_NEARBY_TICKETS
            elif self.state == ST_INITIAL:
                match = re.match(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", line)
                if match:
                    # print(match.groups())
                    self.rules.append(TicketRule(*match.groups()[1:], name=match.groups()[0]))
            elif self.state == ST_YOUR_TICKET:
                if self.myTicket:
                    logger.warning("{}.{}: Duplicated my ticket?".format(
                        self.__class__.__name__, inspect.currentframe().f_code.co_name))
                self.myTicket = [int(num) for num in line.split(',')]
            elif self.state == ST_NEARBY_TICKETS:
                ticket = [int(num) for num in line.split(',')]
                ticketValid = True
                for val in ticket:
                    if not self._isValid(val):
                        self.invalidValueSum += val
                        ticketValid = False
                if ticketValid:
                    self.tickets.append(ticket)
        logger.debug("{}.{}: Valid tickets:\n{}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name,
            '\n'.join([str(ticket) for ticket in self.tickets])))


class TestTicketValidator(unittest.TestCase):
    fInput1a = "input2020_16a.txt"
    fTest1a = "test2020_16a.txt"
    fTest1b = "test2020_16b.txt"
    fTest1c = "test2020_16c.txt"

    def test_MemBank_calculateDepartureTotal_fInput1a_unknown(self):
        tv = TicketValidator()
        tv.readInput(self.fInput1a)
        total = tv.calculateDepartureMultiple()
        print("Departure Field Total: {}".format(total))
        self.assertEqual(3029180675981, total)

    def test_MemBank_calculateDepartureTotal_fInput1a_knownWrongAnswers(self):
        tv = TicketValidator()
        tv.readInput(self.fInput1a)
        total = tv.calculateDepartureMultiple()
        self.assertNotEqual(782, total)
        self.assertNotEqual(1797, total)

    def test_MemBank_invalidTicketCheck_fInput1a(self):
        tv = TicketValidator()
        tv.readInput(self.fInput1a)
        print("Invalid Ticket Num: {}".format(tv.invalidValueSum))
        self.assertEqual(29851, tv.invalidValueSum)

    def test_MemBank_invalidTicketCheck_fTest1a(self):
        tv = TicketValidator()
        tv.readInput(self.fTest1a)
        self.assertEqual(71, tv.invalidValueSum)

    def test_MemBank_printMyTicket_fInput1a(self):
        tv = TicketValidator()
        tv.readInput(self.fInput1a)
        strTicket = tv.printMyTicket()
        self.assertNotEqual("", strTicket)

    def test_MemBank_printMyTicket_fInput1a_knownAnswer(self):
        tv = TicketValidator()
        tv.readInput(self.fInput1a)
        strTicket = tv.printMyTicket()
        self.assertEqual(
            "arrival location: 163, arrival platform: 73, arrival station: 151, arrival track: 193, class: 71, "
            "departure date: 53, departure location: 157, departure platform: 167, departure station: 191, "
            "departure time: 113, departure track: 101, duration: 181, price: 107, route: 127, row: 97, seat: 103, "
            "train: 197, type: 173, wagon: 109, zone: 179", strTicket)

    def test_MemBank_printMyTicket_fTest1b(self):
        tv = TicketValidator()
        tv.readInput(self.fTest1b)
        strTicket = tv.printMyTicket()
        self.assertEqual("class: 12, row: 11, seat: 13", strTicket)

    def test_MemBank_printMyTicket_fTest1c(self):
        tv = TicketValidator()
        tv.readInput(self.fTest1c)
        strTicket = tv.printMyTicket()
        self.assertEqual("class: 12, row: 11, seat: 13", strTicket)


if __name__ == '__main__':
    unittest.main()
