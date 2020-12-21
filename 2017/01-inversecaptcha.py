from base import base


def totalRepeats(fileName):
    firstDigit = None
    total = 0
    for line in base.getInputLines(fileName):
        for char in line:
            currentDigit = int(char)
            if not firstDigit:
                firstDigit = currentDigit
            elif currentDigit == prevDigit:
                total += currentDigit
            prevDigit = currentDigit
    if prevDigit == firstDigit:
        total += firstDigit
    return total


def totalDiametrisFromFile(fileName):
    firstDigit = None
    input = ""
    for line in base.getInputLines(fileName):
        input += line
    return totalDiametricRepeats(input)

def totalDiametricRepeats(line):
    total = 0
    midpoint = len(line) // 2
    for i in range(midpoint):
        if line[i] == line[i + midpoint]:
            total += int(line[i])
    return total * 2


if __name__ == '__main__':
    print("Task1: ", totalRepeats("input2017_01a.txt"))
    print("Task2: ", totalDiametrisFromFile("input2017_01a.txt"))

    print(totalDiametricRepeats("1212"))
