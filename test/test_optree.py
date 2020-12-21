import unittest
from optree import optree


class TestOptree(unittest.TestCase):
    def test_OpTree_independence(self):
        bt = optree.BooleanOpTree()
        dum = optree.DummyOpTree()
        ot = optree.Optree()
        dum.opLookUp["LessEmpty"] = True

        self.assertTrue("LessEmpty" in dum.opLookUp)
        self.assertFalse("LessEmpty" in bt.opLookUp)
        self.assertFalse("LessEmpty" in ot.opLookUp)
        self.assertTrue("LSHIFT" in bt.opLookUp)
        self.assertFalse("LSHIFT" in dum.opLookUp)
        self.assertFalse("LSHIFT" in ot.opLookUp)


class TestBinaryTreePlanter(unittest.TestCase):
    fInputA = "input2017_07a.txt"
    fTestA = "test2017_07a.txt"

    def test_BinaryTreePlanter_fTestA(self):
        expected = {'x': 123, 'y': 456, 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079}
        btp = optree.BinaryTreePlanter(self.fTestA)
        self.assertEqual(expected, btp.evaluatedOutputs)

    def test_BinaryTreePlanter_fInputA(self):
        expected = {'a': 46065, 'aa': 1050, 'ab': 5242, 'ac': 8, 'ad': 65527, 'ae': 5234, 'af': 13555, 'ag': 80}
        btp = optree.BinaryTreePlanter(self.fInputA)
        returnedSubset = {k: v for k, v in sorted(optree.BooleanOpTree.evaluatedOutputs.items())[:8]}
        self.assertEqual(expected, returnedSubset)


if __name__ == '__main__':
    unittest.main()
