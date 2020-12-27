def decode(code):
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

# Functions for unittests
import itertools

def allCodes():
    return [''.join(row + seat) for row in itertools.product("BF", repeat=7) for seat in itertools.product("LR", repeat=3)]

def allCodesShuffled():
    return [''.join(row + seat) for row in itertools.product("BF", repeat=7) for seat in itertools.product("LR", repeat=3)]

def encode(num):
    prefix = format(num // 8, '07b').replace('0', 'F').replace('1', 'B')
    suffix = format(num % 8, '03b').replace('0', 'L').replace('1', 'R')
    return ''.join([prefix, suffix])

