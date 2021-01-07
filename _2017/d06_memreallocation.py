"""
https://adventofcode.com/2017/day/6
"""
from base import base


class MemBalancer:
    def __init__(self, fileName=None):
        self.memState = []
        self.memHistory = {}
        if fileName:
            self.readMemState(fileName)

    def _rebalance(self):
        length = len(self.memState)
        maxValue = max(self.memState)
        index = self.memState.index(maxValue)
        value = self.memState[index]
        # print("".format(length, ))
        self.memState[index] = 0
        for i in range(index + 1, index + value + 1):
            self.memState[i % length] += 1

    def readMemState(self, fileName):
        for line in base.getInputLines(fileName):
            self.memState.extend([int(n) for n in line.split() if n])

    def balance(self):
        count = 0
        while tuple(self.memState) not in self.memHistory:
            self.memHistory[tuple(self.memState)] = count
            self._rebalance()
            count += 1
        return count, self.memHistory[tuple(self.memState)]


if __name__ == '__main__':
    mb = MemBalancer("input2017_06a.txt")
    count, last = mb.balance()
    print("Part 1: {}".format(count))
    print("Part 2: {}".format(count - last))
