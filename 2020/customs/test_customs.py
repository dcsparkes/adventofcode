import customs
import unittest


class TestCustoms(unittest.TestCase):
    def setUp(self):
        self.inputFile = "input.txt"
        self.testFile = "test.txt"

    def test_countSharedAnswers_testFile_counts(self):
        self.assertEqual([3, 0, 1, 1, 1], list(customs.countSharedAnswers(self.testFile)))

    def test_countSharedAnswers_testFile_total(self):
        self.assertEqual(6, sum(customs.countSharedAnswers(self.testFile)))

    def test_countSharedAnswers_inputFile_total(self):
        self.assertEqual(3316, sum(customs.countSharedAnswers(self.inputFile)))

    def test_countUniqueAnswers_testFile_counts(self):
        self.assertEqual([3, 3, 3, 1, 1], list(customs.countUniqueAnswers(self.testFile)))

    def test_countUniqueAnswers_testFile_total(self):
        self.assertEqual(11, sum(customs.countUniqueAnswers(self.testFile)))

    def test_countUniqueAnswers_inputFile_total(self):
        self.assertEqual(6726, sum(customs.countUniqueAnswers(self.inputFile)))

    def test_getAnswers_testFile(self):
        answers = customs.getAnswers(self.testFile)
        self.assertEqual((set(['a', 'b', 'c']), set(['a', 'b', 'c'])), next(answers), 0)
        self.assertEqual((set(['a', 'b', 'c']), set()), next(answers), 1)
        self.assertEqual((set(['a', 'b', 'c']), set(['a'])), next(answers), 2)
        self.assertEqual((set(['a']), set(['a'])), next(answers), 3)
        self.assertEqual((set(['b']), set(['b'])), next(answers), 4)

    def test_sharedAnswers_testFile(self):
        answers = customs.sharedAnswers(self.testFile)
        self.assertEqual(set(['a', 'b', 'c']), next(answers), 0)
        self.assertEqual(set(), next(answers), 1)
        self.assertEqual(set(['a']), next(answers), 2)
        self.assertEqual(set(['a']), next(answers), 3)
        self.assertEqual(set(['b']), next(answers), 4)

    def test_uniqueAnswers_testFile(self):
        answers = customs.uniqueAnswers(self.testFile)
        self.assertEqual(set(['a', 'b', 'c']), next(answers))
        self.assertEqual(set(['a', 'b', 'c']), next(answers))
        self.assertEqual(set(['a', 'b', 'c']), next(answers))
        self.assertEqual(set(['a']), next(answers))
        self.assertEqual(set(['b']), next(answers))

    def test_uniqueAnswers_alternateImplementation_inputFile(self):
        answers = customs.uniqueAnswers(self.inputFile)
        testAnswers = customs.uniqueAnswersOld(self.inputFile)
        for i in range(5):
            self.assertEqual(next(testAnswers), next(answers), i)

    def test_uniqueAnswers_alternateImplementation_testFile(self):
        answers = customs.uniqueAnswers(self.testFile)
        testAnswers = customs.uniqueAnswersOld(self.testFile)
        for i in range(5):
            self.assertEqual(next(testAnswers), next(answers), i)


if __name__ == '__main__':
    unittest.main()
