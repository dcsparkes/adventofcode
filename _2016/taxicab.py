from base import base
from cartesian import cartesian

# base.getLogger(__name__)

def evaluateDirections(fileName, findRepeatVisit=False):
    pos = 0
    t = cartesian.TaxiTracker()
    t.readDirections(fileName)
    if not findRepeatVisit:
        pos = t.pos
    else:
        pos = t.firstIntersection()
    return t.distanceManhattan(pos)

if __name__ == '__main__':
    print("Test: {}\n".format(evaluateDirections("test2016_01d.txt", True)))
    print("Task1: {}".format(evaluateDirections("input2016_01a.txt")))
    print("Task2: {}".format(evaluateDirections("input2016_01a.txt", True)))
