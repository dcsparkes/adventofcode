"""
https://adventofcode.com/2015/day/14
"""
from base import base
import re


class Race:
    def __init__(self, fileName):
        self.deers = None
        self.distances = None
        if fileName:
            self.deers = self.readReindeer(fileName)

    def readReindeer(self, fileName):
        deers = []
        pattern = re.compile("(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")
        for line in base.getInputLines(fileName):
            match = pattern.match(line)
            deers.append(Reindeer(match.group(1), int(match.group(2)), int(match.group(3)), int(match.group(4))))
        return deers

    def raceDistance(self, duration):
        """
        Calculate the distance travelled over a given time interval.

        :param duration:
        :return: Winning reindeer
        """
        winner = None
        for deer in self.deers:
            deer.fullMove(duration)
            if winner and deer.distance < winner.distance:
                pass
            else:
                winner = deer

        return winner

    def raceIterative(self, duration):
        runs = [deer.run() for deer in self.deers]
        for i in range(duration):
            currentWinner = None
            for run in runs:
                deer = next(run)
                if currentWinner and deer.distance < currentWinner.distance:
                    pass
                else:
                    currentWinner = deer
            currentWinner.points += 1
        self.deers.sort()
        return self.deers[-1]


class Reindeer:
    def __init__(self, name, speed, durFlight, durRest):
        self.name = name
        self.durFlight = durFlight
        self.counter = durFlight
        self.durRest = durRest
        self.speed = speed
        self.distance = 0
        self.points = 0
        self.flying = True

    def __lt__(self, other):
        return self.points < other.points

    def __repr__(self):
        return "{}(name='{}', speed={}, durFlight={}, durRest={})".format(self.__class__.__name__, self.name,
                                                                          self.speed, self.durFlight, self.durRest)

    def __str__(self):
        return "{}, distance={}, points={}".format(self.name, self.distance, self.points)

    def fullMove(self, length):
        cycleLength = self.durFlight + self.durRest
        fullCycleCount = length // cycleLength
        remainder = min(length % cycleLength, self.durFlight)
        totalFlightDuration = fullCycleCount * self.durFlight + remainder
        self.distance = totalFlightDuration * self.speed
        return self.distance

    def run(self):
        while True:
            self.counter -= 1
            if self.flying:
                self.distance += self.speed
            if not self.counter:
                self.flying = not self.flying
                if self.flying:
                    self.counter = self.durFlight
                else:
                    self.counter = self.durRest
            yield self


if __name__ == '__main__':
    race1 = Race("input2015_14a.txt")
    print("Winner race 1: {}".format(race1.raceDistance(2503)))
    race2 = Race("input2015_14a.txt")
    print("Winner race 2: {}".format(race2.raceIterative(2503)))