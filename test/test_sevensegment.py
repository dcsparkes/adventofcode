import logging
import unittest

from sevensegment import sevensegment


class MyTestCase(unittest.TestCase):
    fInput = "input2021_08a.txt"
    fTest = "test2021_08a.txt"

    def test_readDigits_entryCount(self):
        entryCount = len(sevensegment.readDigits(self.fTest))
        self.assertEqual(10, entryCount)

    def test_readDigits_isListofTuples(self):
        entries = sevensegment.readDigits(self.fTest)
        with self.subTest(outerType=list):
            self.assertEqual(type(entries), list)
        with self.subTest(elementType=tuple):
            self.assertEqual(type(entries[1]), tuple)

    def test_countUniqueLengthDigits_fTest(self):
        self.assertEqual(26, sevensegment.countUniqueLengthDigits(self.fTest))

    def test_countUniqueLengthDigits_fInput(self):
        self.assertEqual(294, sevensegment.countUniqueLengthDigits(self.fInput))

    def test_evaluateOutput_knownEntry(self):
        knownEntry = (("acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"),
                      ("cdfeb", "fcadb", "cdfeb", "cdbaf"))
        self.assertEqual("5353", sevensegment.evaluateOutput(knownEntry))

    def test_evaluateOutput_invalidPattern_duplicateLengths(self):
        knownBadEntry = (("ac", "ab"), ("acb", "ca"))
        with self.assertRaises(ValueError):
            sevensegment.evaluateOutput(knownBadEntry)

    def test_evaluateOutput_invalidPattern_eightSegments(self):
        knownBadEntry = (("acehgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"),
                         ("cdfeb", "fcadb", "cdfeb", "cdbaf"))
        with self.assertRaises(ValueError):
            sevensegment.evaluateOutput(knownBadEntry)

    def test_evaluateOutput_testData(self):
        entries = sevensegment.readDigits(self.fTest)
        expVals = ["8394", "9781", "1197", "9361", "4873", "8418", "4548", "1625", "8717", "4315"]
        retVals = [sevensegment.evaluateOutput(e) for e in entries]
        self.assertEqual(expVals, retVals)

    def test_evaluateOutput_sum_testData(self):
        entries = sevensegment.readDigits(self.fTest)
        retVals = [int(sevensegment.evaluateOutput(e)) for e in entries]
        self.assertEqual(61229, sum(retVals))

    def test_evaluateOutput_sum_inputData(self):
        entries = sevensegment.readDigits(self.fInput)
        retVals = [int(sevensegment.evaluateOutput(e)) for e in entries]
        self.assertEqual(973292, sum(retVals))

if __name__ == '__main__':
    unittest.main()
