"""
https://adventofcode.com/2021/day/6
"""


class popTracker():
    def __init__(self, initialTimer=0, rebirthTimer=6, firstBirthTimer=8):
        self._reset(initialTimer)
        self.rebirthTimer = rebirthTimer
        self.firstBirthTimer = firstBirthTimer

    def count(self):
        return sum([v for v in self.pops.values()])

    def _insert(self, timer, count):
        if timer in self.pops:
            self.pops[timer] += count
        else:
            self.pops[timer] = count

    def _reset(self, initialTimer=0):
        self.pops = {}
        self._insert(initialTimer, 1)

    def _tick(self):
        self.pops = {t - 1: count for t, count in self.pops.items()}

        if -1 in self.pops:
            self._insert(self.rebirthTimer, self.pops[-1])
            self._insert(self.firstBirthTimer, self.pops[-1])
            del self.pops[-1]

    def trackSinglePop(self, duration):
        """
        Generate an list of population counts from a single lanternfish.  The final population from a given starting
        population can then be calculated, because each fish's reproduction is independent of the others.

        :param duration:
        :return:
        """

        yield self.count()
        for i in range(duration):
            self._tick()
            yield self.count()

    def trackPop(self, initialPop, duration):
        single = list(self.trackSinglePop(duration))
        endPops = [single[-1 - int(x)] for x in initialPop]
        return sum(endPops)

    def bruteForceSolution(self, initialPopTimers, duration):
        """
        Calculate the population by iterating through the reproduction cycle.  Predominantly as a test function or
        performance comparison.

        :param initialPopTimers:
        :param duration:
        :return:
        """
        self.pops = {}
        for t in initialPopTimers:
            self._insert(int(t), 1)

        for i in range(duration):
            self._tick()

        return (self.count())
