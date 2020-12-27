def getInts(fileName):
    with open(fileName) as inFile:
       for line in inFile:
           yield int(line.strip())

def inPreamble(num, preamble):
    for x in preamble:
        if (num - x) in preamble:
            return True
    return False

def findAberration(fileName, preambleSize=5):
    preamble = []
    for num in getInts(fileName):
        if len(preamble) == preambleSize and not inPreamble(num, preamble):
            return num
        preamble.append(num)
        preamble = preamble[-preambleSize:]

def findSequence(fileName, total):
    seq = []
    deficit = -total
    for num in getInts(fileName):
        seq.append(num)    # We know the queue is less than the total so insert a new integer
        deficit += num     # Track the total
        while deficit > 0:
            deficit -= seq[0]
            seq = seq[1:]
        if deficit == 0:
            # print(seq)
            # print(sum(seq))
            return min(seq) + max(seq)


