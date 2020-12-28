"""
https://adventofcode.com/2020/day/6
"""
def getAnswers(fileName):
    uniqueAnswers = set()
    sharedAnswers = set()

    with open(fileName) as inFile:
        for line in inFile:
            newAnswers = set(line.strip())

            if not newAnswers: # Empty line
                yield (uniqueAnswers, sharedAnswers)
                uniqueAnswers.clear()
                sharedAnswers.clear()

            elif not uniqueAnswers: # First Person in Group
                uniqueAnswers = newAnswers
                sharedAnswers = newAnswers

            else:
                uniqueAnswers = uniqueAnswers.union(newAnswers)
                sharedAnswers = sharedAnswers.intersection(newAnswers)

    if len(uniqueAnswers):
         yield (uniqueAnswers, sharedAnswers)

def sharedAnswers(fileName):
    for ansUnique, ansShared in getAnswers(fileName):
        yield ansShared

def uniqueAnswers(fileName):
    for ansUnique, ansShared in getAnswers(fileName):
        yield ansUnique

def countUniqueAnswers(fileName):
    for groupAnswers in uniqueAnswers(fileName):
        yield len(groupAnswers)

def countSharedAnswers(fileName):
    for groupAnswers in sharedAnswers(fileName):
        yield len(groupAnswers)


if __name__ == '__main__':
    fileName = "../input/input2020_06a.txt"
    print("Part One Answer: {}".format(sum(countUniqueAnswers(fileName))))
    print("Part Two Answer: {}".format(sum(countSharedAnswers(fileName))))