"""
Play game of life on a "holey" board
"""
import inspect
import logging
from base import base

logging.basicConfig(filename='../log/lifegame.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Cube:
    """
    3D
    """
    def __init__(self, coordinates):
        if len(coordinates) < 3:
            raise ValueError("Too few dimensions!")
        self.coords = coordinates

    def neighbours(self):
        for i in range(self.coords[0] - 1, self.coords[0] + 2):
            for j in range(self.coords[1] - 1, self.coords[1] + 2):
                for k in range(self.coords[2] - 1, self.coords[2] + 2):
                    coords = (i,j,k)
                    if coords != self.coords:
                        yield coords


class Seat:
    symbols = {False: 'L', True: '#'}
    truths = {value: key for key, value in symbols.items()}

    def __init__(self, symbol='L', coords=None, threshold=4):
        if symbol in self.truths:
            self.occupied = self.truths[symbol]
        else:  # exception?
            logger.warning("Symbol '{}' undefined.".format(symbol))
        self.coords = coords  # stored for debug purposes only
        self.neighboursResolvedOccupiedCount = 0
        self.neighboursUnresolved = []
        self.occupiedNextGen = None
        self.resolved = False
        self.threshold = threshold

    def __repr__(self):
        return "Seat(symbol={})".format(self.symbols[self.occupied])

    def __str__(self):
        return self.symbols[self.occupied]

    def addNeighbour(self, neighbour):
        """
        addNeighbour() should only be called during __init__ phase of game
        :param neighbour: The neighbouring Seat.
        :return: None
        """
        logger.debug("{}.{}: {}-{}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name,
                                           self.coords, neighbour.coords))

        self.neighboursUnresolved.append(neighbour)

    def neighbourIsResolved(self, neighbour):
        """
        Neighbouring seat has 'noticed' that it can never change and has resolved.  This means that no further checks
        need to be made and may cause this Seat to likewise resolve.  To stop cascades of loops/infinite recursion:
            a)  The neighbour is removed from the list first so that changes are not propagated unnecessarily.
            b)  self.resolved is checked because this seat may have already been resolved elsewhere.  This should only
                happen if calcNextGen() has already been called on this object and, subsequently, multiple neighbours
                resolved during calcNextGen() and resolved propagagation

        :param neighbour: Seat object that is now resolved
        :return: None
        """
        self.neighboursUnresolved.remove(neighbour)
        if neighbour.occupied:
            self.neighboursResolvedOccupiedCount += 1
            if not self.resolved and not self.occupied:
                self.resolveSelf()
        else:
            # If there can never be sufficient neighbours to kill the seat
            if not self.resolved and self.occupied and \
                    len(self.neighboursUnresolved) + self.neighboursResolvedOccupiedCount < self.threshold:
                self.resolveSelf()

    def resolveSelf(self):
        """
        Cleanup when Seat is resolved.  Propagate change to neighbours.

        :return: None
        """
        logger.debug("{}.{}: {}: occupied = {}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name,
                                                       self.coords, self.occupied))
        self.resolved = True
        self.occupiedNextGen = self.occupied
        for neighbour in self.neighboursUnresolved:
            neighbour.neighbourIsResolved(self)

    def calcNextGen(self):
        """
        Calculate next status in Game of Life.  Store in self.nextGen.  Calculate whether Seat is resolved and propagate
        accordingly.

        :return: None.
        """
        logger.debug("Starting {}.{}: {}: occupied = {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, self.coords, self.occupied))
        if self.resolved:  # catch those instances where the seat has been resolved through a neighbour's resolution
            logger.info("calcNextGen called on resolved Seat.")

        elif self.occupied:
            # If there can never be sufficient neighbours to kill the seat
            if len(self.neighboursUnresolved) + self.neighboursResolvedOccupiedCount < self.threshold:
                self.resolveSelf()
            # Greater than/equal self.threshold occupied neighbours
            elif [neighbour.occupied for neighbour in self.neighboursUnresolved].count(True) + \
                    self.neighboursResolvedOccupiedCount >= self.threshold:
                # print("Triggered")
                self.occupiedNextGen = False
            else:
                self.occupiedNextGen = True
        # If unoccupied and a neighbour is permanently occupied this seat will never be occupied.
        elif self.neighboursResolvedOccupiedCount:
            self.resolveSelf()
        # If any of the neighbour seats are occupied
        elif [neighbour.occupied for neighbour in self.neighboursUnresolved].count(True):
            self.occupiedNextGen = False
        # If unoccupied and no neighbours are occupied.
        else:
            self.occupiedNextGen = True


        logger.debug("Ending {}.{}: {}: occupied = {}: nextGen = {}: resolved = {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, self.coords, self.occupied,
            self.occupiedNextGen, self.resolved))
        return (self.resolved, self.occupied)

    def iterateGen(self):
        """
        iterateGen() applies the previous calcNextGen() changes to Game of Life.
        The return value is to catch postulated, but unproven theoretical cases where not every seat has resolved, but
        no changes have occurred.  If this case IS possible, it would result in an overcount of the generation number.
        Intuitively, it feels as if resolution will propagate quickly, but, for instance, if the start state IS the
        end state, I'm not 100% certain whether resolved propagation will occur completely.  I think it might, but am
        not certain.

        :return: bool indicating whether the Seat occupancy status has changed.
        """
        logger.debug("{}.{}: {}: occupied = {}: nextGen = {}: resolved = {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, self.coords,
            self.occupied, self.occupiedNextGen, self.resolved))
        retVal = self.occupied != self.occupiedNextGen
        self.occupied = self.occupiedNextGen
        return retVal


class LifeGame:
    def __init__(self, fileName, immediateAdjacency=True, threshold=4):
        logger.debug("{}.{}: {}".format(self.__class__.__name__,
                                        inspect.currentframe().f_code.co_name, fileName))
        self.gen = 0
        self.seatingPlan = []
        self.seatsUnresolved = {}  # {(int, int): Seat}
        # self.seatsAll = {}
        self._populateSeats(fileName, immediateAdjacency, threshold)

    def __eq__(self, other):
        if not isinstance(other, LifeGame):
            return NotImplemented

        retVal = self.seatingPlan == other.seatingPlan
        return self.seatingPlan == other.seatingPlan

    def __ne__(self, other):
        if not isinstance(other, LifeGame):
            return NotImplemented
        retVal = self.seatingPlan != other.seatingPlan
        return self.seatingPlan != other.seatingPlan

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.seatingPlan])

    @staticmethod
    def _bindSeats(seat1, seat2):
        seat1.addNeighbour(seat2)
        seat2.addNeighbour(seat1)

    def _addImmediateNeighbours(self, seat):
        row, col = seat.coords
        if row > 0:
            for i in range(max(0, col - 1), col + 2):
                coord = (row - 1, i)
                if coord in self.seatsUnresolved:
                    self._bindSeats(self.seatsUnresolved[coord], seat)
        if col > 0:
            coord = (row, col - 1)
            if coord in self.seatsUnresolved:
                self._bindSeats(self.seatsUnresolved[coord], seat)

    def _addNonAdjacentNeighbours(self, seat):
        row, col = seat.coords
        directions = {"nw":(-1, -1), "n": (-1, 0), "w": (0, -1), "ne": (-1, +1)}
        listNeighbours = []
        for direction, vector in directions.items():
            for i in range(1, max(row, col)+1):
                coord = (row + vector[0] * i, col + vector[1] * i)
                if coord in self.seatsUnresolved:  # Found first neighbour
                    listNeighbours.append(self.seatsUnresolved[coord])
                    break;
                # elif coord[0] <= 0 or coord[1] <= 0:  # Edge of map
                #     break;

        logger.debug("Ending: {}.{}: neighbours: {}".format(self.__class__.__name__,
                                                            inspect.currentframe().f_code.co_name, listNeighbours))
        for neighbour in listNeighbours:
            self._bindSeats(neighbour, seat)

    def _addSeatToCollective(self, newSeat, immediateAdjacency):
        logger.debug("{}.{}: {}: immediateAdjacency = {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, newSeat.coords, immediateAdjacency))
        self.seatsUnresolved[newSeat.coords] = newSeat
        if immediateAdjacency:
            self._addImmediateNeighbours(newSeat)
        else:
            self._addNonAdjacentNeighbours(newSeat)

    def _populateSeats(self, fileName, immediateAdjacency, threshold):
        logger.debug("Starting: {}.{}: file: {}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name,
                                                        fileName))
        rowID = 0
        for row in base.getInputLines(fileName):
            for colID in range(len(row)):
                if row[colID] == "L" or row[colID] == "#":
                    self._addSeatToCollective(Seat(row[colID], (rowID, colID), threshold), immediateAdjacency)

            self.seatingPlan.append(list(row))
            # print(row)
            rowID += 1
        self.dims = (len(self.seatingPlan), len(self.seatingPlan[0]))
        logger.debug("Ending: {}.{}: Dimensions: {}. # of seats: {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, self.dims, len(self.seatsUnresolved)))

    def calculateNextGen(self):
        logger.debug("Running: {}.{}.  Current generation: {}. # of unresolved seats: {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, self.gen, len(self.seatsUnresolved)))
        for seat in self.seatsUnresolved.values():
            seat.calcNextGen()

    def iterateGen(self):
        logger.debug("Starting: {}.{}.  Current generation = {}. Unresolved Seats = {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, self.gen, len(self.seatsUnresolved)))
        retVal = False
        resolvedSeats = []
        for (rowID, colID), seat in self.seatsUnresolved.items():
            retVal |= seat.iterateGen()
            self.seatingPlan[rowID][colID] = str(seat)
            if seat.resolved:
                resolvedSeats.append((rowID, colID))
        self.gen += 1
        logger.debug("Starting: {}.{}.  Current generation = {}. Unresolved Seats = {}, Resolved Seats = {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, self.gen, self.seatsUnresolved.keys(),
            resolvedSeats))
        for coord in resolvedSeats:
            del self.seatsUnresolved[coord]
        return retVal

    def playGame(self):
        logger.debug("Running: {}.{}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name))
        changing = True
        while (changing):
            print(self, end='\n\n')
            self.calculateNextGen()
            changing = self.iterateGen()

        return str(self).count('#')

    @staticmethod
    def sideBySide(seatA, seatB, separation=5):
        """
        Turn two LifeGames into a single string separated by 'separation' spaces.
        Relatively easy to rewrite with *args for more than 2
        :param seatA:
        :param seatB:
        :param separation:
        :return:
        """
        delimiter = " " * separation
        rowsA = str(seatA).split('\n')
        rowsB = str(seatB).split('\n')
        rows = [delimiter.join(components) for components in zip(rowsA, rowsB)]
        return '\n'.join(rows)


if __name__ == '__main__':
    fTest1a = "test2020_11a.txt"
    fInput1a = "input2020_11a.txt"
    lg1 = LifeGame(fInput1a, immediateAdjacency=True, threshold=4)
    lg2 = LifeGame(fInput1a, immediateAdjacency=False, threshold=5)
    print("Occupied seats = {}".format(lg1.playGame()))
    print("Occupied seats = {}".format(lg2.playGame()))
