import unittest
from _2015 import d17_eggnog


class MyTestCase(unittest.TestCase):
    fInput1a = "input2015_17a.txt"

    def test_init_injectContainers(self):
        injectees = [20, 15, 10, 5, 5]
        cs = d17_eggnog.Containers(containers=injectees)
        self.assertEqual(set(injectees), set(cs.containers))

    def test_init_readContainers_size(self):
        cs = d17_eggnog.Containers(fileName=self.fInput1a)
        self.assertEqual(20, len(cs.containers))

    def test_init_readContainers_type(self):
        cs = d17_eggnog.Containers(fileName=self.fInput1a)
        for c in cs.containers:
            msg = "<{}> is type {}".format(c, type(c))
            self.assertIsInstance(c, int, msg)

    def test_knownResults(self):
        injectees = [20, 15, 10, 5, 5]
        cs = d17_eggnog.Containers(containers=injectees)
        self.assertEqual(4, len(cs.validPermutations(25)))

    def test_fInput1a(self):
        cs = d17_eggnog.Containers(fileName=self.fInput1a)
        self.assertEqual(654, len(cs.validPermutations(150)))


if __name__ == '__main__':
    unittest.main()
