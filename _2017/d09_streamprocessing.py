"""
https://adventofcode.com/2017/day/9
"""
from base import base


class StateMachine:
    def _closeGroup(self):
        self.runningTotal += self.groupValue
        self.groupValue -= 1

    def _countGarbage(self):
        self.garbageCount += 1

    def _openGroup(self):
        self.groupValue += 1

    states = {'RUNNING': {'!': ('RUNNINGBANG', None), '<': ('GARBAGE', None),
                          '{': ('RUNNING', _openGroup), '}': ('RUNNING', _closeGroup), '*': ('RUNNING', None)},
              'GARBAGE': {'!': ('GARBAGEBANG', None), '>': ('RUNNING', None), '*': ('GARBAGE', _countGarbage)},
              'GARBAGEBANG': {'*': ('GARBAGE', None)},
              'RUNNINGBANG': {'*': ('RUNNING', None)}
              }

    def __init__(self, fileName=None):
        self.runningTotal = 0
        self.garbageCount = 0
        self.groupValue = 0
        self.state = 'RUNNING'
        if fileName:
            self.readStream(fileName)

    def inject(self, char):
        stateDict = self.states[self.state]
        if char in stateDict:
            self.state, stateFunc = stateDict[char]
        elif '*' in stateDict:
            self.state, stateFunc = stateDict['*']
        else:
            raise SyntaxError("Unrecognised char '{}' in <{}>".format(char, self.state))

        if stateFunc:
            stateFunc(self)

    def readStream(self, fileName):
        for line in base.getInputLines(fileName):
            for char in line:
                self.inject(char)


if __name__ == '__main__':
    sm = StateMachine("input2017_09a.txt")
    print("Part 1: {}".format(sm.runningTotal))
    print("Part 2: {}".format(sm.garbageCount))
