class Keypad:
    pad1 = (('1', '2', '3'),
            ('4', '5', '6'),
            ('7', '8', '9'),
            )

    start1 = (1, 1)

    pad2 = ((False, False, '1', False, False),
            (False, '2', '3', '4', False),
            ('5', '6', '7', '8', '9'),
            (False, 'A', 'B', 'C', False),
            (False, False, 'D', False, False))
    start2 = (0, 2)

    def __init__(self, keypad=None):
        if not keypad:
            self.keypad = self.pad1
        else:
            self.keypad = keypad
        self.posX = None
        self.posY = None
        self.code = []
        self.reset()

    def readFile(self, fileName):
        with open(fileName) as inFile:
            for line in inFile:
                self.makeMoves(line.strip())
                self.beep()

    def reset(self):
        if self.keypad == self.pad1:
            self.posX, self.posY = self.start1
        elif self.keypad == self.pad2:
            self.posX, self.posY = self.start2

        self.code = []

    def beep(self):
        self.code.append(self.keypad[self.posY][self.posX])

    def getCode(self):
        return ''.join(self.code)

    def inject(self, text):
        for line in text.split('\n'):
            self.makeMoves(line.strip())
            self.beep()

    def _moveDown(self):
        maxY = len(self.keypad) - 1
        if self.posY < maxY and self.keypad[self.posY+1][self.posX]:
            self.posY += 1

    def _moveLeft(self):
        if self.posX > 0 and self.keypad[self.posY][self.posX-1]:
            self.posX -= 1

    def _moveRight(self):
        maxX = len(self.keypad[0]) - 1
        if self.posX < maxX and self.keypad[self.posY][self.posX+1]:
            self.posX += 1

    def _moveUp(self):
        if self.posY > 0 and self.keypad[self.posY-1][self.posX]:
            self.posY -= 1


    def makeMoves(self, line):
        moves = {'D':self._moveDown, 'L':self._moveLeft, 'R':self._moveRight, 'U':self._moveUp}

        # print("{}: {}, {}: {}".format(line, self.posX, self.posY, self.keypad[self.posX][self.posY]))
        for char in line:
            funcMove = moves[char]
            # print(funcMove)
            funcMove()
            # print("{}, {}: {}".format(self.posX, self.posY, self.keypad[self.posX][self.posY]))

            # if char == 'U':
            #     self.posY = max(self.posY - 1, 0)
            # elif char == 'D':
            #     self.posY = min(self.posY + 1, 2)
            # elif char == 'L':
            #     self.posX = max(self.posX - 1, 0)
            # elif char == 'R':
            #     self.posX = min(self.posX + 1, 2)
        # print(self.keypad[self.posX][self.posY])


