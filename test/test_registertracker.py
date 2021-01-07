"""
https://adventofcode.com/2017/day/8
"""
import unittest
from _2017 import d08_registers


class MyTestCase(unittest.TestCase):
    fInput = "input2017_08a.txt"
    fTest1 = "test2017_08a.txt"

    def test_init_fInput_max(self):
        rt = d08_registers.RegisterTracker(self.fInput)
        self.assertEqual(6828, rt.maxRegister())

    def test_init_fInput_maxEver(self):
        rt = d08_registers.RegisterTracker(self.fInput)
        self.assertEqual(7234, rt.maxEverRegister)

    def test_init_fTest1_max(self):
        rt = d08_registers.RegisterTracker(self.fTest1)
        self.assertEqual(1, rt.maxRegister())

    def test_init_fTest1_maxEver(self):
        rt = d08_registers.RegisterTracker(self.fTest1)
        self.assertEqual(10, rt.maxEverRegister)

    def test_init_fTest1_states(self):
        rt = d08_registers.RegisterTracker(self.fTest1)
        self.assertEqual({'a':1, 'b':0, 'c':-10}, rt.registers)



if __name__ == '__main__':
    unittest.main()
