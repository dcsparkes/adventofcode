import itertools

def openInput(fileName):
    with open(fileName) as inFile:
        for line in inFile:
            yield line.strip()

class RecipientTracker:
    def __init__(self):
        self.recipients = {}

    def registerDelivery(self, position):
        if position in self.recipients:
            self.recipients[position] += 1
        else:
            self.recipients[position] = 1

    def countRecipients(self):
        return len(self.recipients.keys())

class Santa:
    def __init__(self, rTracker: RecipientTracker, position=0):
        self.position = complex(position)
        self.rTracker = rTracker
        rTracker.registerDelivery(self.position)

    def move(self, direction):
        self.position += direction
        self.rTracker.registerDelivery(self.position)

class Dispatcher:
    def __init__(self, poolSize=1, posX=0, posY=0):
        self.pool = []
        self.rTracker = RecipientTracker()
        if poolSize < 1:
            raise ValueError("poolSize too small")
        for i in range(poolSize):
            self.pool.append(Santa(self.rTracker, complex(int(posX), int(posY))))

    def convertArrowToComplex(self, arrow):
        direction = None

        if arrow == '^': # Map 'north' to positive real axis
            direction = 1 + 0j
        elif arrow == 'v':
            direction = -1 + 0j
        elif arrow == '>':
            direction = 0 - 1j
        elif arrow == '<': # Map 'west' to positive complex axis
            direction = 0 + 1j

        return direction

    def dispatchCycle(self, fileName):
        santas = itertools.cycle(self.pool)

        with open(fileName) as inFile:
            for line in inFile:
                for direction in map(self.convertArrowToComplex, line):
                    next(santas).move(direction)

    def countRecipients(self):
        return self.rTracker.countRecipients()


# Original implementation: now used as test confirmation
def delivery(fileName):
    posX = 0
    posY = 0
    houses = {}
    houses[(0, 0)] = 1

    for line in openInput(fileName):
        for char in line:
            if char == '^':
                posY += 1
            elif char == 'v':
                posY -= 1
            elif char == '>':
                posX += 1
            elif char == '<':
                posX -= 1
            else:
                continue

            if (posX, posY) in houses:
                houses[(posX, posY)] += 1
            else:
                houses[(posX, posY)] = 1
    return houses

def houseCount(fileName):
    return len(delivery(fileName).keys())



