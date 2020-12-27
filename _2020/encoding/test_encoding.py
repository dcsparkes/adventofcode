import encoding
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fInput = "input9.1.txt"
        self.fTest = "test9.1.txt"


    def test_findAberration_fInput(self):
        self.assertEqual(1721308972, encoding.findAberration(self.fInput, 25))

    def test_findAberration_fTest(self):
        self.assertEqual(127, encoding.findAberration(self.fTest))

    def test_findSequence_fInput(self):
        self.assertEqual(62, encoding.findSequence(self.fInput, 1721308972))

    def test_findSequence_fTest(self):
        self.assertEqual(62, encoding.findSequence(self.fTest, 127))

if __name__ == '__main__':
    unittest.main()
