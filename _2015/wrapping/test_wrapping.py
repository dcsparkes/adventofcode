import wrapping
import unittest


class TestElevator(unittest.TestCase):
    def setUp(self):
        self.fInput = "input2.1.txt"
        self.fTest = "test.txt"

    def test_areas_items_testFile(self):
        answers = wrapping.areas(self.fTest)
        self.assertEqual(58, next(answers), 0)
        self.assertEqual(43, next(answers), 1)

    def test_areas_total_testFile(self):
        self.assertEqual(101, sum(wrapping.areas(self.fTest)))

    def test_areas_total_inputFile(self):
        self.assertEqual(1606483, sum(wrapping.areas(self.fInput)))

    def test_paperArea_1_1_10areas(self):
        self.assertEqual(43, wrapping.paperArea([1, 1, 10]))

    def test_paperArea_2_3_4(self):
        self.assertEqual(58, wrapping.paperArea([2, 3, 4]))

    def test_ribbonLength_1_1_10areas(self):
        self.assertEqual(14, wrapping.ribbonLength([1, 1, 10]))

    def test_ribbonLength_2_3_4(self):
        self.assertEqual(34, wrapping.ribbonLength([2, 3, 4]))

    def test_ribbons_items_testFile(self):
        answers = wrapping.ribbons(self.fTest)
        self.assertEqual(34, next(answers), 0)
        self.assertEqual(14, next(answers), 1)

    def test_ribbons_total_testFile(self):
        self.assertEqual(48, sum(wrapping.ribbons(self.fTest)))

    def test_ribbons_total_inputFile(self):
        self.assertEqual(3842356, sum(wrapping.ribbons(self.fInput)))

    def test_surfaceArea_inputFile(self):
        pass

if __name__ == '__main__':
    unittest.main()
