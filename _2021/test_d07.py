import unittest

from base import base
from d07_treacheryofwhales import calculateFuelCosts, findAveragePosition, findMidpoint


class MyTestCase(unittest.TestCase):
    fInput = "input2021_07a.txt"
    inputData = list(base.getInputLines(fInput, delimiter=',', func=int))
    testData = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    def test_calculateFuelCosts_known1(self):
        self.assertEqual(41, calculateFuelCosts(self.testData, 1))

    def test_calculateFuelCosts_known2(self):
        self.assertEqual(37, calculateFuelCosts(self.testData, 2))

    def test_calculateFuelCosts_known3(self):
        self.assertEqual(39, calculateFuelCosts(self.testData, 3))

    def test_calculateFuelCosts_known10(self):
        self.assertEqual(71, calculateFuelCosts(self.testData, 10))

    def test_calculateFuelCosts_nonlinear_known2(self):
        self.assertEqual(206, calculateFuelCosts(self.testData, 2, nonLinear=True))

    def test_calculateFuelCosts_nonlinear_known5(self):
        self.assertEqual(168, calculateFuelCosts(self.testData, 5, nonLinear=True))

    def test_findAveragePosition_known(self):
        self.assertEqual(5, findAveragePosition(self.testData))

    def test_findMidpoint_simple_odd(self):
        self.assertEqual(3, findMidpoint([1, 2, 3, 4, 5]))

    def test_findMidpoint_simple_even(self):
        self.assertEqual(3, findMidpoint([1, 2, 3, 4, 5, 6]))

    def test_findMidpoint_testData(self):
        self.assertEqual(2, findMidpoint(self.testData))

    def test_integration_inputData(self):
        self.assertEqual(326132, calculateFuelCosts(self.inputData, findMidpoint(self.inputData)))

    def test_integration_testData(self):
        self.assertEqual(37, calculateFuelCosts(self.testData, findMidpoint(self.testData)))

    def test_integration_nonlinear_inputData(self):
        self.assertEqual(88612611,
                         calculateFuelCosts(self.inputData, findAveragePosition(self.inputData), nonLinear=True))

    def test_integration_nonlinear_testData(self):
        self.assertEqual(168, calculateFuelCosts(self.testData, findAveragePosition(self.testData), nonLinear=True))


if __name__ == '__main__':
    unittest.main()
