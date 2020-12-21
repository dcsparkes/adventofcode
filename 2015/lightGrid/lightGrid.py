import inspect
import logging
import re

logger = logging.getLogger(__name__)


def off(x):
    return False


def on(x):
    return True


def toggle(x):
    return not x


def inc(x):
    return x + 1


def dec(x):
    return max(x, 1) - 1


def inc2(x):
    return x+2



class LightGrid:
    def __init__(self, gridSize=(1000, 1000), version=1):
        """
        Create an n-dimensional boolean grid, defaulting to False (Off)
        :param gridSize:    Tuple containing each dimensions, numbered from 0.  No negative or zero dimensions
                            (consider better handling of negatives).  Maybe store coordinates in a dict?
        """
        self.version = version
        t = type(gridSize)
        if t is int or t is float or t is str:
            gridSize = (gridSize,)

        # no negatives, no strings.  Convert iterables to tuples.
        gridSize = tuple([abs(int(x)) for x in gridSize])

        # zero sized dimensions block access to lower dimensions
        if 0 in gridSize:
            logger.warning("{}.{}: gridSize={} contains zero.".format(self.__class__.__name__,
                                                                      inspect.currentframe().f_code.co_name, gridSize))
            gridSize = gridSize[:gridSize.index(0)]

        if not gridSize:
            gridSize = (1,)  # A single point has no dimensions
            logger.info("{}.{}: gridSize={} zero-dimensional grid.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, gridSize))

        self.gridSize = gridSize  # Stored for __repr__
        # Constant fixed co-ordinates: origin; furthest point from origin within grid
        self.origin = (0,) * len(self.gridSize)
        self.maxCoordinates = tuple([x - 1 for x in self.gridSize])
        self.version = version
        default = [None, False, 0][self.version]

        self.grid = self._createGrid(self.gridSize, default=default)  # Passed to recursive function

    def __repr__(self):
        return "{}(gridSize={})".format(__class__.__name__, self.gridSize)

    def __str__(self):
        return str(self.grid).replace("], [", "]\n [").replace("], [", "]\n [")

    def _createGrid(self, dimensions, default=False):  # Timing of 1 vs 2?
        logger.debug("{}.{}(dimensions={})".format(self.__class__.__name__,
                                                   inspect.currentframe().f_code.co_name, dimensions))
        if len(dimensions) == 1:
            retVal = [default] * dimensions[-1]
            logger.debug("{}.{}:len(retVal)={}".format(self.__class__.__name__,
                                                       inspect.currentframe().f_code.co_name, len(retVal)))
        else:
            retVal = [self._createGrid(dimensions[1:]) for i in range(dimensions[0])]
            logger.debug("{}.{}:len(retVal)={}:len(retVal[0])={}".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, len(retVal), len(retVal[0])))
        return retVal

    def _cubeIntersect(self, cornerA, cornerB):
        """
        :param cornerA: Corner of an n-dimensional-cuboid
        :param cornerB: Opposite corner of an n-dimensional-cuboid
        :return:    coordinates as n-dimensional tuples of nearest corner to origin and furthest corner from origin of
                    the n-dimensional cuboid that intersects with the grid of this object. (None, None) if no
                    intersection.
        """
        nearCorner, farCorner = self._sortCorners(cornerA,
                                                  cornerB)  # Discards undefined cases for half-defined dimensions

        # These describe the same cuboid, nearCorner has lower integer values, farCorner has higher integer values.
        origTest, temp = self._sortCorners(self.origin, farCorner)
        temp, maxTest = self._sortCorners(self.maxCoordinates, nearCorner)

        countDim = len(origTest)
        if origTest != self.origin[:countDim] or maxTest != self.maxCoordinates[:countDim]:
            logger.warning("{}.{}: ({}, {}) no intersection with grid.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, cornerA, cornerB))
            return (None, None)
        return self._extrudeCorners(cornerA, cornerB)

    def _extrudeCorners(self, cornerA, cornerB):
        """
        Project or truncate n-dimensional corners into (n±x)-dimensional gridspace.  Dot->Line->Rectangle->Cuboid etc.
        Vice versa, by ignoring later dimensions, the instruction set is a (n-x)-dimensional shadow of the n-dimensional
        hyper-cuboid.
        Alternative implementation is not to extrude into higher dimensions, but then which 'plane' is chosen?  Origin
        plane is probably valid.  Extrusion is at least unambiguous.

        :param cornerA:     m-dimensional co-ordinate tuple of a corner
        :param cornerB:     m-dimensional co-ordinate tuple of b corner
        :return:            List of nearest and furthest corners of the n-dimensional 'cube' described by the
                            input parameter corners.
        """
        # Convert corner vectors to correct dimensions
        countDim = len(self.gridSize)
        nearCorner = cornerA[:countDim] + self.origin[len(cornerA):]  # '+' = Concatenate tuples
        farCorner = cornerB[:countDim] + self.maxCoordinates[len(cornerB):]

        return list(zip(*map(sorted, zip(self.origin, nearCorner, farCorner, self.maxCoordinates))))[1:3]

    def _flipSwitches(self, cornerA, cornerB, funcOperation):
        """
        :param cornerA: n-dimensional co-ordinate tuple of a corner
        :param cornerB: n-dimensional co-ordinate tuple of b corner
        :param funcOperation: on(), off() or toggle() function identifier
        :return: None
        """
        cornerNear, cornerFar = self._cubeIntersect(cornerA, cornerB)
        if cornerNear is not None:
            self._switch(cornerNear, cornerFar, self.grid, funcOperation)
        else:
            logger.info("{}.{}: ({}, {}) no intersection with grid.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, cornerA, cornerB))

    @staticmethod
    def _readLines(fileName):
        with open(fileName) as inFile:
            for line in inFile:
                yield line.strip()

    @staticmethod
    def _sortCorners(cornerA, cornerB):
        """
        :param cornerA: n-dimensional co-ordinate tuple of a corner
        :param cornerB: n-dimensional co-ordinate tuple of b corner
        :return:        list of nearest and furthest corners of the n-dimensional 'cube' described by the
                        input parameter corners.
        """
        if cornerA and cornerB:
            return list(zip(*map(sorted, zip(cornerA, cornerB))))
        else:  # If either vector is zero-dimensional...
            return ((), ())

    def _switch(self, cornerNear, cornerFar, grid, funcOperation):
        logger.debug("switch({}, {}, {}, {}()".format(cornerNear, cornerFar, len(grid), funcOperation.__name__))
        assert len(cornerNear) == len(cornerFar), "Dimension Mismatch between corners."
        # assert len(cornerNear) == len(grid), "Dimension Mismatch between corners and grid."
        if len(cornerNear) == 1:  # Down to a list of lightOn values
            assert type(grid[0]) is bool or type(grid[0]) is int, "Bad type.  Wrong Depth?"
            for i in range(cornerNear[0], cornerFar[0] + 1):
                grid[i] = funcOperation(grid[i])
        else:
            for i in range(cornerNear[0], cornerFar[0] + 1):
                self._switch(cornerNear[1:], cornerFar[1:], grid[i], funcOperation)

    def onCount(self):
        lights = self.grid
        while (lights and type(lights[0]) is list):
            lights = [dim for plane in lights for dim in plane if dim]
        return lights.count(True)

    def _recTotalSum(self, grid):
        if type(grid[0]) is not list:
            return sum(grid)
        else:
            return sum([self._recTotalSum(subgrid) for subgrid in grid])

    def totalSum(self):
        return self._recTotalSum(self.grid)

    def _translateInstructions(self, fileName):
        fLookup = {("turn of", 1):off, ("turn on", 1):on, ("toggle ", 1):toggle,
                   ("turn of", 2):dec, ("turn on", 2):inc, ("toggle ", 2):inc2}

        for line in self._readLines(fileName):
            match = re.findall(r"(\d+),(\d+)", line)
            if (match):
                instruction = fLookup[(line[:7], self.version)]
                cornerA, cornerB = match

                retVal = (tuple([int(x) for x in cornerA]),
                          tuple([int(y) for y in cornerB]),
                          instruction)
                yield retVal

    def readInstructions(self, fileName):
        for cornerA, cornerB, function in self._translateInstructions(fileName):
            self._flipSwitches(cornerA, cornerB, function)

    def toggle(self, cornerA, cornerB):
        self._flipSwitches(cornerA, cornerB, toggle)

    def turnOn(self, cornerA, cornerB):
        self._flipSwitches(cornerA, cornerB, on)

    def turnOff(self, cornerA, cornerB):
        self._flipSwitches(cornerA, cornerB, off)


if __name__ == '__main__':
    import time

    grid = LightGrid((1,))
    print(grid)
    print("=================================================================================================")
    print(grid.onCount())
    print("=================================================================================================")

# █
