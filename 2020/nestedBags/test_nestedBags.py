import logging
import nestedBags
import unittest

class TestNestedBags(unittest.TestCase):
    def setUp(self):
        self.fInput = "input7.1.txt"
        self.fTest1 = "test1.txt"
        self.br = nestedBags.BagRegister()

    def test_BagRegister_readRules_fInput(self):
        self.assertEqual(300, self.br.readRules(self.fInput))

    def test_BagRegister_readRules_fTest1(self):
        self.assertEqual(4, self.br.readRules(self.fTest1))

class TestBag(unittest.TestCase):
    def test_Bag_contains_in(self):
        bag = nestedBags.Bag("red in", contents=[(1, "green"), (1, "blue")])
        self.assertEqual(True, "green" in bag)

    def test_Bag_contains_notIn(self):
        bag = nestedBags.Bag("red notIn", contents=[(1, "green"), (1, "blue")])
        self.assertEqual(False, "orange" in bag)

    def test_Bag_contains_self(self):
        bag = nestedBags.Bag("red self", contents=[(1, "green"), (1, "blue")])
        self.assertEqual(False, "red self" in bag)

class TestBagRegisterInverted(unittest.TestCase):
    def setUp(self):
        self.fInput = "input7.1.txt"
        self.fTest2 = "test2.txt"
        self.bri = nestedBags.BagRegisterInverted()

    def test_BagRegisterInverted_readRules_fInput(self):
        bri = nestedBags.BagRegisterInverted(self.fInput)
        self.assertEqual(8030, bri.result())

    def test_BagRegisterInverted_readRules_fTest2(self):
        bri = nestedBags.BagRegisterInverted(self.fTest2)
        self.assertEqual(126, bri.result())

if __name__ == '__main__':
    logging.basicConfig(filename='test_nestedBags.log', encoding='utf-8', level=logging.INFO)
    unittest.main()
