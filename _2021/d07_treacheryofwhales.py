"""
https://adventofcode.com/2021/day/7
"""

from base import base


def findMidpoint(positions):
    count = len(positions)
    return sorted(positions)[(count - 1) // 2]


def calculateFuelCosts(positions, endPosition, nonLinear=False):
    if not nonLinear:
        costs = [abs(endPosition - p) for p in positions]
    else:
        costs = [(abs(endPosition - p) * (1 + abs(endPosition - p))) // 2 for p in positions]
    return sum(costs)

def findAveragePosition(positions):
    count = len(positions)
    return round((1 + sum(positions)) / count)


if __name__ == '__main__':
    # logging.basicConfig(filename="../log/2021_d07.log", encoding='utf-8', level=logging.WARNING)
    fInput = "input2021_07a.txt"
    # fTest = "test2021_07a.txt"
    inputData = list(base.getInputLines(fInput, delimiter=',', func=int))
    midpoint = findMidpoint(inputData)
    averagePoint = findAveragePosition(inputData)
    fuelCost1 = calculateFuelCosts(inputData, midpoint)
    fuelCost2 = calculateFuelCosts(inputData, averagePoint, nonLinear=True)
    print("inputData cost to move to midpoint({}) is {}.".format(midpoint, fuelCost1))
    print("inputData cost to move to midpoint({}) is {}.".format(averagePoint, fuelCost2))
