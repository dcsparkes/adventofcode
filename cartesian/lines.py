"""
https://adventofcode.com/2021/day/5
"""


class Line():
    def __init__(self, startPoint, endPoint):
        self.startPoint = tuple([int(x) for x in startPoint])
        self.endPoint = tuple([int(x) for x in endPoint])

    def points(self):
        """
        Generate the integer co-ordinates that the line passes through

        :return:
        """
        x1, y1 = self.startPoint
        x2, y2 = self.endPoint
        xdiff = x2 - x1
        ydiff = y2 - y1

        xDirection = xdiff // abs(xdiff) if xdiff else 0
        yDirection = ydiff // abs(ydiff) if ydiff else 0

        iterations = 1 + (xdiff // xDirection) if xdiff else 1 + (ydiff // yDirection) if ydiff else 1

        for i in range(iterations):
            coords = (x1 + (i * xDirection), y1 + (i * yDirection))
            yield coords

