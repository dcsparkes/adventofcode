"""
https://adventofcode.com/2020/day/24
"""
from base import base
from lifegame import cubiclifegame


class Cube2DHex(cubiclifegame.Cube):
    def neighbours(self):
        x, y = self.coords
        for n in self._neigh(self.coords):
            if n != (x + 1, y + 1) and n != (x - 1, y - 1):
                yield n


class TileSet(cubiclifegame.LifeGame):
    referenceCoords = (0, 0)
    machineStates = {'CARDINAL': {'n': ('INTER_N', (-1, 0)), 's': ('INTER_S', (+1, 0)),
                                  'e': ('CARDINAL', (0, +1)), 'w': ('CARDINAL', (0, -1))
                                  },
                     'INTER_N': {'e': ('CARDINAL', (0, +1)), 'w': ('CARDINAL', (0, 0))},
                     'INTER_S': {'e': ('CARDINAL', (0, 0)), 'w': ('CARDINAL', (0, -1))}
                     }  # Unnecessary third state... could be merged by changing CARDINAL moves to include y axis shift

    def __init__(self, fileName=None):
        self.flippedTiles = []
        super().__init__(fileName, cubeClass=Cube2DHex, spawnRanges=(2, 2), surviveRanges=(1, 2))

    def flip(self, instructions):
        current = self.referenceCoords
        ms = 'CARDINAL'
        for c in instructions:
            if c not in self.machineStates[ms]:
                msg = "Unexpected character '{}' in machine state <{}>: {}.".format(c, ms, line)
                raise SyntaxError(msg)
            else:
                ms, move = self.machineStates[ms][c]
                current = tuple(map(sum, zip(current, move)))

        if ms != 'CARDINAL':
            msg = "Unexpected line termination in machine state <{}>: {}".format(ms, line)
            raise SyntaxError(msg)
        else:
            if current in self.flippedTiles:
                self.flippedTiles.remove(current)
            else:
                self.flippedTiles.append(current)

    def flippedCount(self):
        return len(self.flippedTiles)

    def readMyFlips(self, fileName):
        """
        No new taxes.
        :return:
        """

        for line in base.getInputLines(fileName):
            self.flip(line)

    def _populateCubes(self, fileName):
        self.readMyFlips(fileName)
        for coord in self.flippedTiles:
            self.activeCubes.append(Cube2DHex(coord))
