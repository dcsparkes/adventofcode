"""
https://adventofcode.com/2021/day/8
"""
import logging
import sys

from base import base

logging.basicConfig(filename="../log/sevensegment.log", encoding='utf-8', level=logging.WARNING)


def readDigits(fileName):
    entries = []
    for line in base.getInputLines(fileName):
        prepatterns, preoutput = line.split('|')
        entries.append((tuple(prepatterns.split()), tuple(preoutput.split())))
    return entries


def countUniqueLengthDigits(fileName):
    """
    Count the frequency of digits with 2, 3, 4 or 7 segments (digits 1, 7, 4 & 8 respectively) in the oupyt section of
    the entries.

    :param fileName:
    :return:
    """
    return sum([1 for entry in readDigits(fileName) for o in entry[1] if len(o) in [2, 3, 4, 7]])


def sumOutputs(fileName):
    """
    Task 2
    :param fileName:
    :return:
    """
    return sum([int(evaluateOutput(e)) for e in readDigits(fileName)])


TOP, UL, UR, MID, LL, LR, BOT = range(7)


class letterToSegmentMapper():
    segmentMappings = {0: {TOP, UL, UR, LL, LR, BOT},
                       1: {UR, LR},
                       2: {TOP, UR, MID, LL, BOT},
                       3: {TOP, UR, MID, LR, BOT},
                       4: {UL, UR, MID, LR},
                       5: {TOP, UL, MID, LR, BOT},
                       6: {TOP, UL, MID, LL, LR, BOT},
                       7: {TOP, UR, LR},
                       8: {TOP, UL, UR, MID, LL, LR, BOT},
                       9: {TOP, UL, UR, MID, LR, BOT}
                       }

    def __init__(self, entry):
        logging.debug("{}.{}(entry={})".format(self.__class__.__name__, sys._getframe().f_code.co_name, entry))
        self.digitsByLength = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}
        self.patternToDigitMap = {}
        patterns = set([''.join(sorted(p)) for p in entry[0]])
        self.outputs = [''.join(sorted(o)) for o in entry[1]]
        combined = sorted(patterns | set(self.outputs), key=len)

        uniqueChars = set(''.join(combined))
        if len(uniqueChars) > 7:
            msg = "Too many ({}) unique characters \"{}\" in: {}.".format(len(uniqueChars),
                                                                          ''.join(sorted(uniqueChars)), entry)
            raise (ValueError(msg))
        self.letterToSegmentMap = {l: set(range(7)) for l in uniqueChars}
        self._mapPatternsToDigits(combined)

    def _allocateDigitToPattern(self, pattern, digit):
        logging.debug(
            "{}.{}(pattern=\"{}\", digit={})".format(self.__class__.__name__, sys._getframe().f_code.co_name, pattern,
                                                     digit))
        self.patternToDigitMap[pattern] = digit
        self.digitsByLength[len(pattern)].remove(digit)
        self._updateLetterToSegmentMap(pattern, digit)

    def _illuminatedSegments(self, pattern):
        """
        DEPRECATED for self._segmentState()
        Return a list of lit segments.

        First look at all of the segment references.  If a segment state is shown in a non-pattern letter then its
        state is undefined.  Otherwise it must be lit.
        :param pattern:
        :return:
        """
        undefined = set([segment for key in self.letterToSegmentMap.keys() if key not in pattern
                         for segment in self.letterToSegmentMap[key]])
        return set(range(7)) - undefined

    def _segmentState(self, pattern):
        """
        Return a list/dict with state information about the segments based on the pattern.
        True = Definitely lit, i.e. pattern contains every letter that might illuminate that segment.
        False = Definitely unlit, i.e. segment is not referenced by any pattern letter.
        None = Undefined, i.e. some of the illuminating letters are not in the pattern.
        :param pattern:
        :return:
        """
        referenceCountInMap = [0] * 7
        referenceCountInPattern = [0] * 7
        for key in self.letterToSegmentMap.keys():
            for segment in self.letterToSegmentMap[key]:
                referenceCountInMap[segment] += 1
        for letter in pattern:
            for segment in self.letterToSegmentMap[letter]:
                referenceCountInPattern[segment] += 1
        return [(False if not referenceCountInPattern[i] else
                 (True if referenceCountInPattern[i] == referenceCountInMap[i] else None)) for i in range(7)]

    def _eliminateCandidate(self, candidate, states):
        """
        Given a candidate and some state information, can we eliminate the candidate from the list of possibilities?
        :param candidate: A digit
        :param states: The known state of the segments (True = lit, False = unlit, None = unknown)
        :return: True if candidate is impossible, False, if still possible
        """
        for segment in range(7):
            if states[segment] is None:
                pass
            elif (states[segment]) ^ (segment in self.segmentMappings[candidate]):
                return True
            # elif states[segment] and segment not in self.segmentMappings[candidate]:  # Could use an XOR!
            #     return True
            # elif not states[segment] and segment in self.segmentMappings[candidate]:
            #     return True
        return False

    def _inferDigitFromPattern(self, pattern):
        candidates = self.digitsByLength[len(pattern)]

        # Determine which segments must be illuminated, or are unilluminated, if known.
        states = self._segmentState(pattern)

        # Eliminate impossible candidates
        return [c for c in candidates if not self._eliminateCandidate(c, states)]

    def _updateLetterToSegmentMap(self, pattern, digit):
        segments = self.segmentMappings[digit]
        logMsg = "{}.{}(pattern=\"{}\", digit={}): segments={}: letterToSegmentMaps:\n\t" \
                 "Pre = {}".format(self.__class__.__name__, sys._getframe().f_code.co_name, pattern, digit, segments,
                                   self.letterToSegmentMap)
        for letter in self.letterToSegmentMap.keys():
            if letter in pattern:
                self.letterToSegmentMap[letter] &= segments
            else:
                self.letterToSegmentMap[letter] -= segments
        logging.debug("{}\n\tPost = {}".format(logMsg, self.letterToSegmentMap))

    def _mapPatternsToDigits(self, patterns):
        """
        Examine the patterns and allocate the correct digits to each pattern.20

        At the moment the function loops through the patterns once and doesn't test that the puzzle is solved.  It
        really feels as if I should either test for unallocated patterns or, more weakly/efficiently, at least test
        whether the output patterns have been identified and reloop if they haven't (do-while equivalent / tail
        recursion).

        I feel like there might be some edge cases where either 1, 4 or 7 are missing, in which 2, 3, 5 can't be
        uniquely identified and 0, 6, 9 might be.

        So I have included said code, but it has not been run as the examples worked without it.  In reality the test /
        input data has all ten digits so 2, 3 & 5 are always uniquely distinguishable due to 1 & 4.

        :param patterns:
        :return:
        """
        unallocatedPatterns = []

        for p in patterns:
            pLength = len(p)
            possibleDigits = self.digitsByLength[pLength]
            # print("{} is len {}.  Possible Values = {}".format(p, pLength, possibleDigits))
            if len(possibleDigits) > 1:
                possibleDigits = self._inferDigitFromPattern(p)
                if not possibleDigits:
                    msg = "Pattern Error \"{}\": all candidates eliminated".format(p)
                    raise (ValueError(msg))

            if len(possibleDigits) == 1:
                self._allocateDigitToPattern(p, possibleDigits[0])

            elif not len(possibleDigits):
                msg = "Pattern Error: {} contains too many patterns of length {}".format(patterns, pLength)
                raise (ValueError(msg))
            else:
                unallocatedPatterns.append(p)

        if unallocatedPatterns:
            logging.warning(
                "{}.{}() Unallocated patterns: {}".format(self.__class__.__name__, sys._getframe().f_code.co_name,
                                                          unallocatedPatterns))
            outputSolved = [o not in unallocatedPatterns for o in self.outputs]
            if False in outputSolved:
                self._mapPatternsToDigits(unallocatedPatterns)

    def output(self):
        return ''.join([str(self.patternToDigitMap[o]) for o in self.outputs])


def evaluateOutput(entry):
    unallocatedDigits = set(range(10))

    lsm = letterToSegmentMapper(entry)
    return lsm.output()
