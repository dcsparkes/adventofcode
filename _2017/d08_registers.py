"""
https://adventofcode.com/2017/day/8
"""
from base import base
import operator
import re


class RegisterTracker:
    lookup = {'==': operator.eq, '>': operator.gt, '>=': operator.ge, '<': operator.lt, '<=': operator.le,
              '!=': operator.ne}
    regex = re.compile(r"(\w+) (\w\wc) ([-]?\d+) if (\w+) ([=!<>]{1,2}) ([-]?\d+)")

    def __init__(self, fileName=None):
        self.maxEverRegister = 0
        self.registers = {}
        if fileName:
            self.readInstructions(fileName)

    def _applyInstruction(self, line):
        match = self.regex.match(line)
        if match:
            varTarget = match.group(1)
            if varTarget not in self.registers:
                self.registers[varTarget] = 0
            varTest = match.group(4)
            if varTest not in self.registers:
                self.registers[varTest] = 0
            opFunc = self.lookup[match.group(5)]
            if opFunc(self.registers[varTest], int(match.group(6))):
                changeValue = int(match.group(3))
                if match.group(2) == "inc":
                    self.registers[varTarget] += changeValue
                elif match.group(2) == "dec":
                    self.registers[varTarget] -= changeValue
                else:
                    raise ValueError("Unrecognised operator: {}".format(match.group(2)))
                if self.registers[varTarget] > self.maxEverRegister:
                    self.maxEverRegister = self.registers[varTarget]

    def readInstructions(self, fileName):
        for line in base.getInputLines(fileName):
            self._applyInstruction(line)

    def maxRegister(self):
        return max(self.registers.values())


if __name__ == '__main__':
    rt = RegisterTracker("input2017_08a.txt")
    print("Part 1: {}".format(rt.maxRegister()))
    print("Part 2: {}".format(rt.maxEverRegister))
