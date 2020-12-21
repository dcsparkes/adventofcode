class Triangles:
    def __init__(self):
        self.candidates = []
        self.triangles = []

    def count(self):
        return len(self.triangles)

    def pivot(self):
        self.triangles = []
        for i in range(0, len(self.candidates), 3):
            candsUnpivoted = self.candidates[i:i+3]
            # print("{}: {} : {}".format(i, candsUnpivoted, list(zip(*candsUnpivoted))))
            for cand in zip(*candsUnpivoted):
                if self._validateTriangle(cand):
                    self.triangles.append(cand)

    def readFile(self, fileName):
        with open(fileName) as inFile:
            for line in inFile:
                tSides = [int(x) for x in line.strip().split(' ') if x]
                self.candidates.append(tSides)
                if self._validateTriangle(tSides):
                    self.triangles.append(tSides)

    @staticmethod
    def _validateTriangle(sides):
        ss = sorted(sides)
        return sum(ss[:-1]) > ss[-1]