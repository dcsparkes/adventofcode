from base import base
import unittest


# class TestLogging(unittest.TestCase):
#     fileTest1 = "base01.txt"
#     linesTest = ["101", "202", "303", "505"]
#
#     def test_deprecatedFunctionsWarn_getInts(self):
#         linesInput = base.getInputLines(self.fileTest1, int)
#         for lineTest in self.linesTest:
#             self.assertEqual(int(lineTest), next(linesInput))


class TestBaseFunctions(unittest.TestCase):
    fileTest1 = "base01.txt"
    linesTest = ["101", "202", "303", "505"]

    def test_getInputLines_base01(self):
        linesInput = base.getInputLines(self.fileTest1)
        for lineTest in self.linesTest:
            self.assertEqual(lineTest, next(linesInput))

    def test_deprecatedFunction_getInts_base01(self):
        linesInput = base.getInts("../input/" + self.fileTest1)
        for lineTest in self.linesTest:
            self.assertEqual(int(lineTest), next(linesInput))

    def test_getInputLines_asInt_base01(self):
        linesInput = base.getInputLines(self.fileTest1, func=int)
        for lineTest in self.linesTest:
            self.assertEqual(int(lineTest), next(linesInput))



if __name__ == '__main__':
    unittest.main()
