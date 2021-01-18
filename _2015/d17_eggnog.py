"""
https://adventofcode.com/2015/day/17
"""
from base import base
import logging


class Containers:
    def __init__(self, fileName=None, containers=None):
        self.containers = None
        if fileName:
            self.readContainers(fileName)
        elif containers:
            self.injectContainers(containers)

    def injectContainers(self, containers):
        """
        initialise
        :param containers:
        :return:
        """
        self.containers = sorted(containers)

    def readContainers(self, fileName):
        self.containers = [container for container in base.getInputLines(fileName, func=int)]
        self.containers.sort()

    def _validPerms(self, containers, volume):
        ps = []
        head = containers[0]
        tail = containers[1:]
        if head > volume:
            pass
        else:
            if head == volume:
                ps.append([head])
            if tail:
                ps.extend(self._validPerms(tail, volume))
                for p in self._validPerms(tail, volume - head):
                    p.append(head)
                    ps.append(p)
        return ps

    def validPermutations(self, volume):
        return self._validPerms(self.containers, volume)

    def minimumLenPermutations(self, value):
        ps = [len(p) for p in self.validPermutations(value)]
        countMin = min(ps)
        return ps.count(countMin)


if __name__ == '__main__':
    cs = Containers("input2015_17a.txt")
    print("Part 1: {}".format(len(cs.validPermutations(150))))
    print("Part 2: {}".format(cs.minimumLenPermutations(150)))
