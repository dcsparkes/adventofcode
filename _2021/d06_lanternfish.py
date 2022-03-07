"""
https://adventofcode.com/2021/day/6
"""

from base import base
from lanternfish import lanternfish

def lanternfishGrowth(duration, initialTimer=0, rebirthTimer=6, firstBirthTimer=8):
    """

    Generate an array such that each position is the population count from a single lanternfish.  The final population
    from a given starting population can be calculated, because each fish's reproduction is independent of the others.

    Pretty sure this could be calculated mathematically, or, at the very least in reverse using functional algorithms.

    :param duration: Number of lifecycles
    :param initialTimer: 
    :param rebirthTimer: Timer value when lanternfish gives birth, i.e. normal gestation period
    :param firstBirthTimer: Timer value when lanternfish is born, i.e. maturity period
    :return:
    """
    # pops = [1] * (rebirthTimer - 1)
    # iterations = 1 + duration // rebirthTimer
    # for i in range(iterations + 1):
    #     newPop = pops[-1] + pops[-3]
    #     pops.extend([newPop] * rebirthTimer)
    #
    # return pops

    pops = [(initialTimer, 1)]


if __name__ == '__main__':
    # logging.basicConfig(filename="../log/2021_d06.log", encoding='utf-8', level=logging.WARNING)
    fInput = "input2021_06a.txt"
    # fTest = "test2021_06a.txt"

    p = lanternfish.popTracker()
    initialTimers = list(base.getInputLines(fInput, delimiter=','))
    print("After {} days, there will be {} lanternfish.".format(80, p.trackPop(initialTimers, 80)))
    p = lanternfish.popTracker()
    print("After {} days, there will be {} lanternfish.".format(256, p.trackPop(initialTimers, 256)))
