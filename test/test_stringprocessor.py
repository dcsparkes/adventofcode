import unittest
from base import base
from stringprocessor import stringprocessor


class TestStringDecoder(unittest.TestCase):
    fsTest = ["test2015_08a.txt", "test2015_08b.txt"]

    lines = [line for fileName in fsTest for line in base.getInputLines(fileName)]
    expecteds = [0, 3, 7, 1, 2, 2, 6]
    # ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"', '"\\\\\\xf3"', '"\\\\\\""', '"b\\\\\\\\xda"']
    # [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"', r'"\\\xf3"', r'"\\\""', r'"b\\\\xda"']
    # print(lines)

    sd = stringprocessor.StringDecoder()

    def test_processLine_abc_fromFile(self):
        processed = self.sd.processLine(self.lines[1])
        self.assertEqual(3, len(processed))

    def test_processLine_abc_fromString(self):
        processed = self.sd.processLine('\"abc\"')
        self.assertEqual(3, len(processed))

    def test_processLine_abc_fromString2(self):
        processed = self.sd.processLine('"abc"')
        self.assertEqual(3, len(processed))

    def test_processLine_empty_fromFile(self):
        processed = self.sd.processLine(self.lines[0])
        self.assertEqual(0, len(processed))

    def test_processLine_empty_fromString(self):
        processed = self.sd.processLine('\"\"')
        self.assertEqual(0, len(processed))

    def test_processLine_empty_fromString2(self):
        processed = self.sd.processLine('""')
        self.assertEqual(0, len(processed))

    def test_processLine_allFromFile(self):
        for i in range(len(self.lines)):
            processed = self.sd.processLine(self.lines[i])
            msg = "{}: {}: <{}>, <{}>".format(i, self.expecteds[i], self.lines[i], processed)
            self.assertEqual(self.expecteds[i], len(processed), msg)


class TestStringEncoder(unittest.TestCase):
    fsTest = ["test2015_08a.txt", "test2015_08b.txt"]
    se = stringprocessor.StringEncoder()
    def test_processLine_allFromFile(self):
        for i in range(len(self.lines)):
            processed = self.sd.processLine(self.lines[i])
            msg = "{}: {}: <{}>, <{}>".format(i, self.expecteds[i], self.lines[i], processed)
            self.assertEqual(self.expecteds[i], len(processed), msg)



if __name__ == '__main__':
    unittest.main()
