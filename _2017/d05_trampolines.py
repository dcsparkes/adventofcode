"""
https://adventofcode.com/2017/day/5
"""
from base import base


class BouncingAnt:
    def __init__(self, fileName=None):
        self.maze = []
        if fileName:
            self.readFile(fileName)

    def readFile(self, fileName):
        self.maze = [int(i) for i in base.getInputLines(fileName, func=int)]

    def runMaze(self, dec=False):
        pos = 0
        maze = self.maze[:]
        count = 0
        while 0 <= pos < len(maze):
            yield count, pos
            newPos = pos + maze[pos]
            if maze[pos] >= 3 and dec:
                maze[pos] -= 1
            else:
                maze[pos] += 1
            count += 1
            pos = newPos


if __name__ == '__main__':
    ba = BouncingAnt("input2017_05a.txt")
    for count, pos in ba.runMaze():
        pass
    print("Part 1: {}".format(count + 1))
    for count, pos in ba.runMaze(dec=True):
        pass
    print("Part 2: {}".format(count + 1))
