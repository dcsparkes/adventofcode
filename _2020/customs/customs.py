def getAnswers(fileName):
    uniqueAnswers = set()
    sharedAnswers = set()

    with open(fileName) as inFile:
        for line in inFile:
            newAnswers = set(line.strip())
            # print(newAnswers)

            if not newAnswers: # Empty line
                # print("END: unique: {} shared: {} new: {}".format(uniqueAnswers, sharedAnswers, newAnswers))
                yield (uniqueAnswers, sharedAnswers)
                uniqueAnswers.clear()
                sharedAnswers.clear()

            elif not uniqueAnswers: # First Person in Group
                # print("FIRST: unique: {} shared: {} new: {}".format(uniqueAnswers, sharedAnswers, newAnswers))
                uniqueAnswers = newAnswers
                sharedAnswers = newAnswers
                # print("unique: {} shared: {}".format(uniqueAnswers, sharedAnswers))

            else:
                # print("unique: {} shared: {} new: {}".format(uniqueAnswers, sharedAnswers, newAnswers))
                uniqueAnswers = uniqueAnswers.union(newAnswers)
                sharedAnswers = sharedAnswers.intersection(newAnswers)
                # print("unique: {} shared: {}".format(uniqueAnswers, sharedAnswers))

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


# Unittest functions
def uniqueAnswersOld(fileName):
    chars = set()
    with open(fileName) as inFile:
        for line in inFile:
            cs = line.strip()
            if len(cs):
                for c in cs:
                    chars.add(c)
            elif len(chars):
                yield chars
                chars.clear()
    if len(chars):
        yield chars
