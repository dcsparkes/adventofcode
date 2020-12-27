import joltage
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.fInput = "input2020_10a.txt"
        self.fTestA = "test2020_10a.txt"
        self.fTestB = "test2020_10b.txt"

    def test_task1_fInput(self):
        self.assertEqual(2080, joltage.task1(self.fInput))

    def test_task1_fTestA(self):
        self.assertEqual(35, joltage.task1(self.fTestA))

    def test_task1_fTestB(self):
        self.assertEqual(220, joltage.task1(self.fTestB))

    def test_task2_fInput(self):
        self.assertEqual(6908379398144 , joltage.task2(self.fInput))

    def test_task2_fTestA(self):
        self.assertEqual(8, joltage.task2(self.fTestA))

    def test_task2_fTestB(self):
        self.assertEqual(19208, joltage.task2(self.fTestB))

if __name__ == '__main__':
    unittest.main()
