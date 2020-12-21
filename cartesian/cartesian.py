import inspect
import logging
from base import base

logging.basicConfig(filename='../log/{}.log'.format(__name__), level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Tracker:
    def __init__(self, heading='E'):
        self.pos = 0
        self.intersections = []
        self.positionHistory = {}

    def currentPos(self):
        print("cP: {}".format(self.pos))
        return self.pos

    def currentDist(self):
        return self.distanceManhattan(self.pos)

    def firstIntersection(self):
        if self.intersections:
            return self.intersections[0]


class MatrixTracker(Tracker):
    pass


class ComplexTracker(Tracker):
    rotations = {'L': +1j, 'R': -1j}
    shifts = {'N': 1, 'S': -1, 'E': -1j, 'W': +1j}
    revShifts = {value: key for key, value in shifts.items()}  # debug

    def __init__(self):
        logger.debug("{}: ComplexTracker.{}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name))
        self.transformationFuncs = {'L': self._rotate, 'R': self._rotate, 'F': self._forward,
                                    'N': self._shift, 'S': self._shift, 'E': self._shift, 'W': self._shift}
        self.heading = self.shifts['E']
        self.pos = 0
        self.positionHistory = {self.pos: True}

    def _forward(self, direction, value):
        return (self.heading, value)

    def _rotate(self, instruction, value):
        move = 0
        count = 0
        self.heading *= self.rotations[instruction] ** (value // 90)
        logger.debug("{}.{}: New Heading: Pair:{}{}: Pos {}: heading: {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, instruction, value, self.pos, self.heading))
        return (move, count)

    def _move(self, move, count):
        startPos = self.pos
        self.pos += move * count
        logger.debug("{}.{}: startPos: {}. move :{}. endPos: {}.".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, startPos, move * count, self.pos))

    def _shift(self, instruction, value):
        logger.debug("{}.{}: Pair:{}{}: pos: {}. _shift :{}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, instruction, value, self.pos,
            self.shifts[instruction]))
        return (self.shifts[instruction], value)

    @staticmethod
    def distanceManhattan(pos):
        # print("dM: {}".format(pos))
        if pos:
            return int(abs(pos.real) + abs(pos.imag))

    def getDistance(self):
        logger.debug("{}.{}: {}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name, self.pos))
        return self.distanceManhattan(self.pos)

    # numsAsDegrees - L90 is a 90 degree turn, not numsAsDegrees - L90 means _rotate left and move 90
    def readDirections(self, fileName):
        move = None
        for pair in base.getInputLines(fileName, delimiter=', '):
            direction = pair[0]
            value = int(pair[1:])
            logger.debug("{}: Pos: {}: Heading:{}".format(pair, self.pos, self.heading))
            func = self.transformationFuncs[direction]

            self._move(*func(direction, value))
        # print("End: {} ".format(self.pos))


class TaxiTracker(ComplexTracker):
    """
    Probably should move intersection tracking here.
    """

    def __init__(self):
        logger.debug("{}: TaxiTracker.{}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name))
        ComplexTracker.__init__(self)
        self.intersections = []

    def _move(self, move, count):
        for i in range(count):
            logger.debug("Move: pos: {}. move :{}.".format(self.pos, move))
            self.pos += move

            if self.pos in self.positionHistory:
                self.intersections.append(self.pos)
            else:
                self.positionHistory[self.pos] = True

    def _rotate(self, direction, value):
        """
        Rotate the taxi in preparation to move forward value steps.
        :param direction:
        :param value:
        :return:
        """
        self.heading *= self.rotations[direction]
        return (self.heading, value)


class WaypointTracker(ComplexTracker):
    def __init__(self):
        logger.debug("{}.{}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name))
        ComplexTracker.__init__(self)
        # Self.heading is the position of the waypoint
        self.heading = 10 * self.shifts['E'] + self.shifts['N']

    def _shift(self, instruction, value):
        """
        Shift only moves the waypoint, not the ship.
        :param instruction: N, S, E, or W, translated to a unit _shift
        :param value: Amount of units
        :return:
        """
        oldHeading = self.heading
        self.heading += self.shifts[instruction] * value
        logger.debug("{}.{}: Pair:{}{}: oldHeading = {}, newHeading = {}.".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, instruction, value,
            oldHeading, self.heading))
        return (0, 0)

    def waypointDistance(self):
        return self.distanceManhattan(self.waypointPosAbsolute())

    def waypointPosAbsolute(self):
        return self.pos + self.heading


if __name__ == '__main__':
    pass
