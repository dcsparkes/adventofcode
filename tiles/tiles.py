"""
Play a jigsaw of square tiles
"""


class Tile:
    def __init__(self, buffer):
        # print(buffer)
        self.id = int(buffer[0][5:])
        self.tile = buffer[1:]
        self.dims = (len(self.tile), len(self.tile[0]))
        self.sideIDs = [None] * 4
        self._calculateSides()

    def __repr__(self):
        return "{}(id={}, dims={})".format(self.__class__.__name__, self.id, self.dims)

    def __str__(self):
        return '\n'.join(self.tile)

    @staticmethod
    def sideToIDs(code):
        """
        Return the int value and its matching complement (i.e. reversed value) sorted in value order for comparisons.
        :param code: The side as a string of '#' and '.' chars,
        :return:    To sort or not to sort?  Sorting aids matching and is flip independent, but not sorting allows
                    state information about chirality to be maintained.  Sorting for simplicity, but chirality might
                    need to be encoded separately.
        """
        bin = code.replace('.', '0').replace('#', '1')
        value = int(bin, 2)
        complement = int(bin[::-1], 2)
        return tuple(sorted([value, complement]))

    def _calculateSides(self):
        self.sideIDs[0] = self.sideToIDs(self.tile[0])
        self.sideIDs[2] = self.sideToIDs(self.tile[-1])
        zipped = [''.join(row) for row in zip(*self.tile)]
        self.sideIDs[3] = self.sideToIDs(zipped[0])
        self.sideIDs[1] = self.sideToIDs(zipped[-1])

    def flipHorizontal(self):
        self.tile = [row[::-1] for row in self.tile]

    def flipVertical(self):
        self.tile.reverse()

    def rotate90(self):
        self.tile = [''.join(row) for row in zip(*reversed(self.tile))]
        self.sideIDs = self.sideIDs[3:] + self.sideIDs[:3]

    def rotate180(self):
        self.tile = reversed([row[::-1] for row in self.tile])
        self.sideIDs = self.sideIDs[2:] + self.sideIDs[:2]

    def rotate270(self):
        self.tile = [''.join(row) for row in reversed(list(zip(*self.tile)))]
        self.sideIDs = self.sideIDs[1:] + self.sideIDs[:1]

    def __str__(self):
        return '\n'.join(self.tile)


class Dealer:
    def __init__(self, fileName):
        self.playGame(fileName)
        self.tiles = []

    def readTiles(fileName):
        tileBuffer = []
        for line in base.getInputLines(fileName):
            print(line)
            if not line:
                pass

            elif not tileBuffer and line[:4] == "Tile":
                yield Tile(tileBuffer)
                tileBuffer.clear()
                tileBuffer.append(line)

            else:
                tileBuffer.append(line)

        yield Tile(tileBuffer)

    def playGame(fileName):
        for tile in readTiles(fileName):
            self.tiles.insert(tile)
            print(tile)
