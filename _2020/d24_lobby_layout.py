"""
https://adventofcode.com/2020/day/24
"""
from lobbylayout import lobbylayout

if __name__ == '__main__':
    ts = lobbylayout.TileSet('..\input\input2020_24a.txt')
    print("Part 1: {}".format(ts.flippedCount()))
    genCounts = ts.playGame(100)
    print("Part 2: {}".format(genCounts[-1]))
