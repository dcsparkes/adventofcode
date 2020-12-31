"""
Play a jigsaw of square tiles
https://adventofcode.com/2020/day/20
"""
from base import base


class Tile:
    def __init__(self, buffer):
        self.id = int(buffer[0].strip('Tile :'))
        self.tile = buffer[1:]
        self.dims = (len(self.tile), len(self.tile[0]))
        self.sideIDs = [None] * 4
        self.edges = []
        self._calculateSides()

    def __repr__(self):
        return "{}(id={}, dims={})".format(self.__class__.__name__, self.id, self.dims)

    def __str__(self):
        return '\n'.join(self.tile)

    def _calculateSides(self):
        self.sideIDs[0] = self.sideToIDs(self.tile[0])
        self.sideIDs[2] = self.sideToIDs(self.tile[-1])
        zipped = [''.join(row) for row in zip(*self.tile)]
        self.sideIDs[3] = self.sideToIDs(zipped[0])
        self.sideIDs[1] = self.sideToIDs(zipped[-1])

    def align(self, topID, leftID):
        funcs = [None, self.rotate270, self.rotate180, self.rotate90]
        if topID:
            orientation = self.sideIDs.index(topID)
            if orientation:
                funcs[orientation]()  # Rotate topID to top

            if leftID is None:
                if self.sideIDs[3] not in self.edges:
                    self.flipHorizontal()
                    if self.sideIDs[3] not in self.edges:
                        raise ValueError("Invalid Rotation: {}, {}".format(topID, leftID))

            elif self.sideIDs[3] != leftID:
                self.flipHorizontal()
                if self.sideIDs[3] != leftID:
                    raise ValueError("Invalid Rotation: {}, {}".format(topID, leftID))
        else:  # if not topID
            orientation = (1 + self.sideIDs.index(leftID)) % 4
            if orientation:
                funcs[orientation]()  # Rotate leftID to left

            if self.sideIDs[0] not in self.edges:
                self.flipVertical()
                if self.sideIDs[0] not in self.edges:
                    raise ValueError("Invalid Rotation: {}, {}".format(topID, leftID))

    @staticmethod
    def concatenateTileRow(tileRow, delimiter='  ') -> str:  # Mainly for debug
        return '\n'.join([delimiter.join(row) for row in zip(*[t.tile for t in tileRow])])

    @staticmethod
    def concatenateTrimmedTileRow(tileRow) -> list:
        """
        Strip the border and concatenate the tiles into a list of lines, 1 per height of the tile
        :param tileRow: A list of Tile objects
        :return: A list of str
        """
        return [''.join([str(tr[1:-1]) for tr in trs]) for trs in list(zip(*[t.tile for t in tileRow]))[1:-1]]

    def _translatePatternToRegExPattern(self, pattern):
        """

        :param pattern: lines
        :return: regular expression
        """
        regExes = []
        for line in pattern:
            line.replace(' ', '.')
            regExes.append(line.replace(' ', '.'))

    def _patternMatch(self, coords, pattern):
        """
        Check if the tile matches the pattern at the coordinates given.

        :param coords: x, y coordinate within tile.
        :param pattern:
        :return:
        """
        patWidth = len(pattern[0])
        patHeight = len(pattern)
        x0, y0 = coords
        for y1 in range(patHeight):
            for x1 in range(patWidth):
                if pattern[y1][x1] == '#':
                    if self.tile[y0 + y1][x0 + x1] != '#':
                        return False
        return True

    def _findPatternMatches(self, pattern):
        """
        On a particular orientation of the tile find matches to the pattern.
        :param pattern:
        :return:
        """
        patWidth = len(pattern[0])
        patHeight = len(pattern)
        for x in range(self.dims[0] - patWidth):
            for y in range(self.dims[1] - patHeight):
                if self._patternMatch((x, y), pattern):
                    yield (x, y)

    def countSymbol(self, symbol):
        return sum([line.count(symbol) for line in self.tile])


    def findPattern(self, pattern):
        """
        Find instances of the pattern on the tile.  Cycle through every orientation and see if there are any matches.
        Assumptions:    The pattern matches only in one orientation.
        :param pattern:
        :return:
        """
        for t in self.spin():
            matches = [match for match in t._findPatternMatches(pattern)]
            if matches:
                return matches

    def flipHorizontal(self):
        self.tile = [row[::-1] for row in self.tile]
        swap = self.sideIDs[1]
        self.sideIDs[1] = self.sideIDs[3]
        self.sideIDs[3] = swap

    def flipVertical(self):
        self.tile.reverse()
        swap = self.sideIDs[2]
        self.sideIDs[2] = self.sideIDs[0]
        self.sideIDs[0] = swap

    def rotate90(self):
        self.tile = [''.join(row) for row in zip(*reversed(self.tile))]
        self.sideIDs = self.sideIDs[3:] + self.sideIDs[:3]

    def rotate180(self):
        self.tile = reversed([row[::-1] for row in self.tile])
        self.sideIDs = self.sideIDs[2:] + self.sideIDs[:2]

    def rotate270(self):
        self.tile = [''.join(row) for row in reversed(list(zip(*self.tile)))]
        self.sideIDs = self.sideIDs[1:] + self.sideIDs[:1]

    @staticmethod
    def sideToIDs(code):
        """
        Return the int value and its matching complement (i.e. reversed value) sorted in value order for comparisons.
        :param code: The side as a string of '#' and '.' chars,
        :return:    To sort or not to sort?  Sorting aids matching and is flip independent, but not sorting allows
                    state information about chirality to be maintained.  Sorting for simplicity, but chirality might
                    need to be encoded separately.
        """
        binary = code.replace('.', '0').replace('#', '1')
        value = int(binary, 2)
        complement = int(binary[::-1], 2)
        return tuple(sorted([value, complement]))

    def spin(self):
        """
        Rotate and flip to all 8 possible orientations
        :return:
        """
        for f in range(2):
            for i in range(4):
                yield self
                self.rotate90()
            self.flipHorizontal()


class Dealer:
    puzzle: Tile

    def __init__(self, fileName):
        self.tiles = []
        self.count = 0
        self.dims = None
        self.sideIndices = {}
        self.cornerResult = None
        self.puzzle = None
        self._setup(fileName)

    @staticmethod
    def _findDims(num):
        """
        Find the dimensions of the puzzle in tiles.  Assume square.
        :param num: Number of tiles.
        :return:  Tuple of (x, y) dimensions.
        """
        root = int(num ** 0.5)
        return (root, root)

    def _findEdges(self):
        self.corners = []
        for ind in self.sideIndices:
            if len(self.sideIndices[ind]) == 1:  # Edge
                tile = self.sideIndices[ind][0]
                tile.edges.append(ind)
                if len(tile.edges) == 2:
                    self.corners.append(tile)

    def _findNextTile(self, prev, tileId):
        pair = self.sideIndices[tileId]
        if pair[0] == prev:
            return pair[1]
        else:
            return pair[0]

    @staticmethod
    def _readTiles(fileName):
        tileBuffer = []
        for line in base.getInputLines(fileName):
            # print(line)
            if not line:
                pass

            elif line[:4] == "Tile" and tileBuffer:
                yield Tile(tileBuffer)
                tileBuffer.clear()
                tileBuffer.append(line.strip())

            else:
                tileBuffer.append(line.strip())

        yield Tile(tileBuffer)

    def _registerSides(self, tile):
        for index in tile.sideIDs:
            if index not in self.sideIndices:
                self.sideIndices[index] = [tile]
            else:
                self.sideIndices[index].append(tile)

    def _setup(self, fileName):
        for tile in self._readTiles(fileName):
            self.tiles.append(tile)
            self._registerSides(tile)
            self.count += 1

        self.dims = self._findDims(self.count)  # for now assume square
        self._findEdges()

    def assemblePuzzle(self):
        """
        Put the tiles together.  Because the IDs are unique chirality is not an issue.  Arbitrarily pick a corner
        and puzzle orientation, orient up and left, then proceed column by column, row by row, orienting up and
        left.  Requires two functions in Tile: align() to rotate and flip the tile to match orientation and trim()
        to take off the edges.
        Additional function to put the tiles together so that they can be assembled into one big tile.

        :return: assembled puzzle with edges removed
        """
        start = self.corners[0]
        # print(start.sideIDs)
        # print(start.edges)
        start.align(*start.edges)
        # print(start.sideIDs)
        # print(start.edges)

        # Populate Top Edge
        puzzle = [[start]]
        row = 0
        for col in range(1, self.dims[0]):
            prevTile = puzzle[row][-1]
            leftID = prevTile.sideIDs[1]
            nextTile = self._findNextTile(prevTile, leftID)
            nextTile.align(topID=None, leftID=leftID)
            puzzle[row].append(nextTile)
        # Populate Left Edge
        col = 0
        for row in range(1, self.dims[1]):
            prevTile = puzzle[-1][col]
            topID = prevTile.sideIDs[2]
            nextTile = self._findNextTile(prevTile, topID)
            nextTile.align(topID=topID, leftID=None)
            puzzle.append([nextTile])
        # Populate main body
        for row in range(1, self.dims[1]):
            for col in range(1, self.dims[0]):
                prevTile = puzzle[row][-1]
                aboveTileID = puzzle[row - 1][col].sideIDs[2]
                leftID = prevTile.sideIDs[1]
                nextTile = self._findNextTile(prevTile, leftID)
                nextTile.align(topID=aboveTileID, leftID=leftID)
                puzzle[row].append(nextTile)

        tileDefBuffer = [str(self.calculateCornerMultiple())]
        for tileRow in puzzle:
            tileDefBuffer.extend(Tile.concatenateTrimmedTileRow(tileRow))
        self.puzzle = Tile(tileDefBuffer)

    def calculateCornerMultiple(self):
        cornerResult = 1
        if len(self.corners) == 4:
            for corner in self.corners:
                cornerResult *= corner.id
        return cornerResult

    def findSerpents(self):
        serpentPattern = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
        count = self.puzzle.findPattern(serpentPattern)
        return count
