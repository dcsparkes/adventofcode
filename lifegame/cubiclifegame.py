"""
Play Game of Life on an n-dimensional board:
https://adventofcode.com/2020/day/17
"""
import inspect
import logging
from base import base

logging.basicConfig(filename='../log/lifegame.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Cube:
    """
    An n-dimensional cube in n-dimensional space.  At the moment this is a superclass, because I haven't tested the
    n-dimensional neighbours() function that nicely yields a series of coordinates.
    """
    def __init__(self, coordinates, n=None):
        """
        Pad out and truncate the Cube co-ordinates to n-dimensions
        :param coordinates: tuple containing the co-ordinates.
        :param n: number of dimensions
        """
        if n is None:
            n = len(coordinates)

        self.coords = (coordinates + (0,) * n)[:n]

    def __repr__(self):
        return "Cube(coordinates={})".format(str(self.coords))

    def __str__(self):
        return str(self.coords)

    def neighbours(self):
        for coord in _neigh(self, coords):
            yield coord

    def _neigh(self, coords):
        if not coords:
            yield tuple()
        else:
            for i in range(self.coords[0] - 1, self.coords[0] + 2):
                for coord in self._neigh(coords[1:]):
                    yield (i, ) + coord



class Cube3D(Cube):
    """
    3D
    """

    def __init__(self, coordinates):
        super().__init__(coordinates, 3)

    def neighbours(self):
        for i in range(self.coords[0] - 1, self.coords[0] + 2):
            for j in range(self.coords[1] - 1, self.coords[1] + 2):
                for k in range(self.coords[2] - 1, self.coords[2] + 2):
                    yield (i, j, k)  # includes self to ensure dict entry, but remove for calculation


class Cube4D(Cube):
    """
    4D
    """

    def __init__(self, coordinates):
        super().__init__(coordinates, 4)

    def neighbours(self):
        for i in range(self.coords[0] - 1, self.coords[0] + 2):
            for j in range(self.coords[1] - 1, self.coords[1] + 2):
                for k in range(self.coords[2] - 1, self.coords[2] + 2):
                    for m in range(self.coords[3] - 1, self.coords[3] + 2):
                        yield (i, j, k, m)  # includes self to ensure dict entry, but remove for calculation


class LifeGame:
    def __init__(self, fileName, iterations=6, cubeClass=Cube3D):
        self.activeCubes = []
        self.neighbourCounts = {}
        self.cubeClass = cubeClass  # Some sort of type checking: isInstance(Cube)?
        self._populateCubes(fileName)
        self._playGame(iterations)

    @classmethod
    def threeD(cls, fileName, iterations=6):
        return cls(fileName, iterations, cubeClass=Cube3D)

    @classmethod
    def fourD(cls, fileName, iterations=6):
        return cls(fileName, iterations, cubeClass=Cube4D)

    def _populateCubes(self, fileName):
        logger.debug("Starting: {}.{}: file: {}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name,
                                                        fileName))
        rowID = 0
        for row in base.getInputLines(fileName):
            for colID in range(len(row)):
                if row[colID] == "#":
                    self.activeCubes.append(self.cubeClass((rowID, colID)))  # Cube auto-pads out additional dimensions
            rowID += 1
        logger.debug("Ending: {}.{}: # of cubes: {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, len(self.activeCubes)))

    def _populateNeighbourCounts(self):
        self.neighbourCounts = {}  # .clear()
        for cube in self.activeCubes:
            for neighbour in cube.neighbours():
                if neighbour in self.neighbourCounts:
                    self.neighbourCounts[neighbour] += 1
                else:
                    self.neighbourCounts[neighbour] = 1

    def _evaluateActiveCubes(self):
        for cube in self.activeCubes[:]:
            count = self.neighbourCounts[cube.coords] - 1  # remove 'self' neighbouring
            if 2 <= count <= 3:  # cube survives
                pass
            else:  # cube dies
                self.activeCubes.remove(cube)
            del self.neighbourCounts[cube.coords]  # don't create a new cube at these coords

    def _spawnNewCubes(self):
        for coord, value in self.neighbourCounts.items():
            if value == 3:
                self.activeCubes.append(self.cubeClass(coord))

    def _playGame(self, iterationCount):
        self._populateNeighbourCounts()
        cubeCounts = []

        for generation in range(iterationCount):
            self._populateNeighbourCounts()
            cubeCounts.append(len(self.activeCubes))
            self._evaluateActiveCubes()
            self._spawnNewCubes()

        cubeCounts.append(len(self.activeCubes))
        logger.debug("Ending: {}.{}: Cube counts by generation: {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, cubeCounts))

    def getActiveCubeCount(self):
        return len(self.activeCubes)
