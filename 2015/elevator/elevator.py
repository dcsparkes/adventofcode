def openInput(fileName):
    with open(fileName) as inFile:
        for line in inFile:
            yield line.strip()

def parenthesesCount(fileName):
    runningCount = 0
    for line in openInput(fileName):
        runningCount += line.count('(')
        runningCount -= line.count(')')

    return runningCount

def parenthesesMismatch(fileName):
    position = 0
    moveCount = 0

    for line in openInput(fileName):
        for char in line:
            if char == '(':
                position += 1
                moveCount += 1
            elif char == ')':
                position -= 1
                moveCount += 1

            if position == -1:
                return moveCount
    return None




