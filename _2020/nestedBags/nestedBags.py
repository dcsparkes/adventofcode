import inspect
import logging
import re

class Bag():
    def __init__(self, colour, total=1, contents=[]):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("{}.{}(\"{}\", total={}, contents={})".format(self.__class__.__name__,
                                                                        inspect.currentframe().f_code.co_name,
                                                                        colour, total, contents))
        self.colour = colour
        self.calculatedTotal = total
        self.uncalculatedBranches = contents

    def __repr__(self):
        return "<Bag: {}, {}, {}>".format(self.colour, self.calculatedTotal, self.uncalculatedBranches)

    def __str__(self):
        return "<Bag: {}, {}, {}>".format(self.colour, self.calculatedTotal, self.uncalculatedBranches)

    def resolve(self, bagList):
        self.logger.debug("{}.{}({})".format(self.__class__.__name__,
                                             inspect.currentframe().f_code.co_name, bagList))
        self.logger.debug("Start condition: \"{}\".{}({})".format(self.colour, self.calculatedTotal, self.uncalculatedBranches))

        # print(self.uncalculatedBranches)
        for mult, colour in list(self.uncalculatedBranches):
            for bag in bagList:
                if bag.colour == colour:
                    self.calculatedTotal += bag.total() * int(mult)
                    self.uncalculatedBranches.remove((mult, colour))
        self.logger.debug("End condition: \"{}\".{}({})".format(self.colour, self.calculatedTotal, self.uncalculatedBranches))


    def total(self):
        if self.uncalculatedBranches:
            return None
        else:
            return self.calculatedTotal

    def __contains__(self, item):
        if self.uncalculatedBranches:
            return item in list(zip(*self.uncalculatedBranches))[1]
        else:
            return False

class BagRegisterInverted():
    def __init__(self, fileName=None):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("{}.{}({})".format(self.__class__.__name__,
                                             inspect.currentframe().f_code.co_name, fileName))
        self.bagsUnresolved = []
        self.bagsResolved = []
        self.bagsCompleted = [] # Probably unnecessary... why not just delete resolved & propagated bags?
        self.shinyGoldBag = None
        if fileName:
            self.readRules(fileName)

    def result(self):
        self.logger.debug("{}.{}()".format(self.__class__.__name__, inspect.currentframe().f_code.co_name))
        if self.shinyGoldBag:
            return self.shinyGoldBag.total() - 1

    def interpretRule(self, rule):
        self.logger.debug("{}.{}({})".format(self.__class__.__name__, inspect.currentframe().f_code.co_name, rule))
        colour, contents = rule.split(" bags contain ")
        match = re.findall(r"(\d+) ([a-z ]*) bag", contents)
        # print(match)
        if not match: # "... bags contain no other bags."
            self.bagsResolved.append(Bag(colour))
            # print(self.bagsResolved[-1])
        else:
            self.bagsUnresolved.append(Bag(colour, contents=match))
            # print(self.bagsUnresolved[-1])

    def readRules(self, fileName):
        self.logger.debug("{}.{}({})".format(self.__class__.__name__,
                                                   inspect.currentframe().f_code.co_name, fileName))
        with open(fileName) as inFile:
            for rule in inFile:
                self.interpretRule(rule.lower().strip())

        self.logger.debug("Before Solve():\nbagsUnresolved:{}\nbagsResolved:{}\nbagsCompleted:{}".format(
            self.bagsUnresolved, self.bagsResolved, self.bagsCompleted))
        self.solve()

        # self.shinyGoldBag = self.bagsUnresolved["shiny gold"]

        return self.result()

    def solve(self):
        """Solution 1:  iterate across resolved bags,
                        incrementally resolve unresolved bags, move resolved bags to completed.
                        Always resolvable, may not find a solution => no solution.
                        Orphan trees calculated.
                        O(n^2)
           Solution 2:  Construct net of contained bags, fill up from resolved bags.
                        Orphan trees calculated.
                        O(n.log(n))
           Solution 3:  Construct net of contained bags, fill down tree from gold bag.
                        Orphan trees not calculated.
                        O(n.log(n))
                        Potential hitch: unresolvability. O(n.log(n))
           """
        self.logger.debug("{}.{}()".format(self.__class__.__name__, inspect.currentframe().f_code.co_name))

        # Passes
        i = 1
        while(self.bagsResolved):
            self.logger.debug("Before Pass {}:\nbagsUnresolved:{}\nbagsResolved:{}\nbagsCompleted:{}".format(
                i, self.bagsUnresolved, self.bagsResolved, self.bagsCompleted))
            pending = self.bagsResolved
            self.bagsResolved = []

            for bag in list(self.bagsUnresolved):
                bag.resolve(pending)
                if bag.total():
                    self.bagsResolved.append(bag)
                    self.bagsUnresolved.remove(bag)
                    if bag.colour == "shiny gold":
                        self.shinyGoldBag = bag

            # print("pending:{} completed:{}".format(pending, self.bagsCompleted))
            self.bagsCompleted.extend(pending)
            # print("pending:{} completed:{}".format(pending, self.bagsCompleted))

            self.logger.debug("After Pass {}:\nbagsUnresolved:{}\nbagsResolved:{}\nbagsCompleted:{}".format(
                i, self.bagsUnresolved, self.bagsResolved, self.bagsCompleted))

class BagRegister():
    def __init__(self):
        self.bagsDeadEnd = {}
        self.bagsDefinite = {}
        self.bagsUndecided = {}

    def test(self, bag, match):
        definiteLink = False
        # print("test: {} : {}".format(bag, match))
        for c in match:
            if c in self.bagsDefinite:
                definiteLink = True
                break

        if definiteLink:
            self.bagsDefinite[bag] = match
        else:
            possibleLinks = [colour for colour in match if colour not in self.bagsDeadEnd]
            if possibleLinks:
                self.bagsUndecided[bag] = possibleLinks
            else:
                self.bagsDeadEnd[bag] = possibleLinks

    def recalculate(self):
        startLen = len(self.bagsUndecided)
        keys = list(self.bagsUndecided.keys())
        for key in keys:
            self.test(key, self.bagsUndecided.pop(key))
        return (startLen - len(self.bagsUndecided)) and len(self.bagsUndecided)

    def interpretRule(self, rule):
        bag, contents = rule.split(" bags contain ")
        match = re.findall(r"\d ([a-z ]*) bag", contents)

        if not match: # "... bags contain no other bags."
            self.bagsDeadEnd[bag] = []
        elif "shiny gold" in match:
            self.bagsDefinite[bag] = match
        else:
            self.test(bag, match)

    def readRules(self, fileName):
        with open(fileName) as inFile:
            for rule in inFile:
                self.interpretRule(rule.lower().strip())

        # print("Dead Ends: {}".format(self.bagsDeadEnd.keys()))
        # print("Definite: {}".format(self.bagsDefinite.keys()))
        # print("Undecided: {}".format(self.bagsUndecided.keys()))
        while (self.recalculate()):
            pass
            # print("Dead Ends: {}".format(self.bagsDeadEnd.keys()))
            # print("Definite: {}".format(self.bagsDefinite.keys()))
            # print("Undecided: {}".format(self.bagsUndecided.keys()))

        return(len(self.bagsDefinite))
