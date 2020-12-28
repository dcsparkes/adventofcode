"""
https://adventofcode.com/2020/day/5
"""

def decode(code):
    """
    Convert seat code into binary and then into int.
    :param code: str containing position info
    :return: int ID corresponding to position code
    """
    return int(code.replace('L', '0').replace('R', '1').replace('F', '0').replace('B', '1'), 2)

def highestSeat(fileName):
    maxID = 0
    with open(fileName) as inFile:
        for line in inFile:
            maxID = max(maxID, decode(line.strip()))

    return maxID

def missingSeat(fileName):
    ids = []
    missingIDs = []
    with open(fileName) as inFile:
        for line in inFile:
            ids.append(decode(line.strip()))

    ids.sort()
    prev = ids[0]
    for id in ids[1:]:
        # print(id)
        if (id - prev) > 1:
            missingIDs.append(prev + 1)
            return prev + 1
        prev = id


if __name__ == '__main__':
    print("Highest Seat ID: {}".format(highestSeat("../input/input2020_05a.txt")))
    print("Your Seat ID: {}".format(missingSeat("../input/input2020_05a.txt")))
