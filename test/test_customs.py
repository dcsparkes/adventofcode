import unittest
from _2020 import d06_customs


# Unittest functions
def uniqueAnswersOld(fileName):
    chars = set()
    with open(fileName) as inFile:
        for line in inFile:
            cs = line.strip()
            if len(cs):
                for c in cs:
                    chars.add(c)
            elif len(chars):
                yield chars
                chars.clear()
    if len(chars):
        yield chars


class TestCustoms(unittest.TestCase):
    def setUp(self):
        self.inputFile = "../input/input2020_06a.txt"
        self.testFile = "../input/test2020_06a.txt"

    def test_countSharedAnswers_testFile_counts(self):
        self.assertEqual([3, 0, 1, 1, 1], list(d06_customs.countSharedAnswers(self.testFile)))

    def test_countSharedAnswers_testFile_total(self):
        self.assertEqual(6, sum(d06_customs.countSharedAnswers(self.testFile)))

    def test_countSharedAnswers_inputFile_total(self):
        self.assertEqual(3316, sum(d06_customs.countSharedAnswers(self.inputFile)))

    def test_countUniqueAnswers_testFile_counts(self):
        self.assertEqual([3, 3, 3, 1, 1], list(d06_customs.countUniqueAnswers(self.testFile)))

    def test_countUniqueAnswers_testFile_total(self):
        self.assertEqual(11, sum(d06_customs.countUniqueAnswers(self.testFile)))

    def test_countUniqueAnswers_inputFile_total(self):
        self.assertEqual(6726, sum(d06_customs.countUniqueAnswers(self.inputFile)))

    def test_getAnswers_testFile(self):
        answers = d06_customs.getAnswers(self.testFile)
        self.assertEqual((set(['a', 'b', 'c']), set(['a', 'b', 'c'])), next(answers), 0)
        self.assertEqual((set(['a', 'b', 'c']), set()), next(answers), 1)
        self.assertEqual((set(['a', 'b', 'c']), set(['a'])), next(answers), 2)
        self.assertEqual((set(['a']), set(['a'])), next(answers), 3)
        self.assertEqual((set(['b']), set(['b'])), next(answers), 4)

    def test_sharedAnswers_testFile(self):
        answers = d06_customs.sharedAnswers(self.testFile)
        self.assertEqual(set(['a', 'b', 'c']), next(answers), 0)
        self.assertEqual(set(), next(answers), 1)
        self.assertEqual(set(['a']), next(answers), 2)
        self.assertEqual(set(['a']), next(answers), 3)
        self.assertEqual(set(['b']), next(answers), 4)

    def test_uniqueAnswers_testFile(self):
        answers = d06_customs.uniqueAnswers(self.testFile)
        self.assertEqual(set(['a', 'b', 'c']), next(answers))
        self.assertEqual(set(['a', 'b', 'c']), next(answers))
        self.assertEqual(set(['a', 'b', 'c']), next(answers))
        self.assertEqual(set(['a']), next(answers))
        self.assertEqual(set(['b']), next(answers))

    def test_uniqueAnswers_alternateImplementation_inputFile(self):
        answers = d06_customs.uniqueAnswers(self.inputFile)
        testAnswers = uniqueAnswersOld(self.inputFile)
        for i in range(5):
            self.assertEqual(next(testAnswers), next(answers), i)

    def test_uniqueAnswers_alternateImplementation_testFile(self):
        answers = d06_customs.uniqueAnswers(self.testFile)
        testAnswers = uniqueAnswersOld(self.testFile)
        for i in range(5):
            self.assertEqual(next(testAnswers), next(answers), i)


if __name__ == '__main__':
    unittest.main()
