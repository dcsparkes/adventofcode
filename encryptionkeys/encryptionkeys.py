"""
https://adventofcode.com/2020/day/25
"""

class TransformSequence:
    def __init__(self, subject=7):
        self.subject = subject
        self.value = 1

    def __iter__(self):
        self.value = 1
        return self

    def __next__(self):
        self.value = self.transform(self.subject, self.value)
        return self.value

    @staticmethod
    def transform(subject, value=1):
        return (value * subject) % 20201227

class EncryptionKeyFinder:
    def __init__(self, *args):
        self.publicKeys = args
        self.loopSizes = EncryptionKeyFinder.findLoopSizes(args)
        self.encryptionKey = self.calculateEncryptionKey(args)

    def calculateEncryptionKey(self, publicKeys):
        ts = TransformSequence(self.publicKeys[0])
        for i in range(self.loopSizes[1]):
            key = next(ts)
        return key

    @staticmethod
    def findLoopSizes(publicKeys):
        keyCount = len(publicKeys)
        loopSizes = [0] * keyCount
        count = 0
        ts = TransformSequence()

        for value in TransformSequence():
            count += 1
            for i in range(keyCount):
                if publicKeys[i] == value:
                    loopSizes[i] = count
            if 0 not in loopSizes:
                return tuple(loopSizes)



