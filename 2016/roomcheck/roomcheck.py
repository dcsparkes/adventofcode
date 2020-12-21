import re


class Room:
    """
    A Room returns True if it is valid.
    Rooms can be added as if they are ints: sectorID is used
    """

    def __init__(self, definition="", nameEncoded="", sectorID=0, isValid=False):
        self.sectorID = sectorID
        self.isValid = isValid
        self.nameEncoded = nameEncoded
        self.name = ""

        if definition:
            self._processDefinition(definition)

        if self.isValid and self.nameEncoded and self.sectorID:
            self.name = self._decodeName(self.nameEncoded, self.sectorID)
            self.name = self._decodeName(self.nameEncoded, self.sectorID)

    def __add__(self, other):
        return self.sectorID + other

    __radd__ = __add__

    # def __radd__(self, other):
    #     return self.sectorID + other

    def __bool__(self):
        return self.isValid

    def __repr__(self):
        return "Room(name={}, sectorID={}, isValid={})".format(self.name, self.sectorID, self.isValid)

    def __str__(self):
        return str((self.name, self.sectorID, self.isValid))

    @staticmethod
    def _generateChecksum(chars):
        """
        Generate a checksum
        :param chars: string of char types, i.e. a string
        :return: checksum of input parameter as defined in AoC 2016 day 4
        """
        charCount = {}
        while (chars):
            charCount[chars[0]] = -chars.count(chars[0])  # count occurrences of first character (make -ve for sorting)
            chars = chars.replace(chars[0], '')  # delete all occurrences of first character
            # print("{}:{}".format(chars, charCount))

        # Ascending sort by value (highest negative first) then key (alphabetical).  Assign first 5 pairs to countSorted
        countSorted = sorted([(value, key) for key, value in charCount.items()])[0:5]
        #  Unzip to estract chars in correct order and join() them to form checksum string
        return ''.join(list(zip(*countSorted))[1])

    @staticmethod
    def _decodeName(encoded, rotation):
        lookup = Room._makeLookup(rotation)
        name = ''.join([lookup[c] for c in encoded])
        # print(name)

        return name

    @staticmethod
    def _makeLookup(rotation):
        lookup = {'-': ' ', ' ': '-'}  # fixed 'rotations': reciprocal for unittesting
        alphas = "abcdefghijklmnopqrstuvwxyz"
        rotation %= len(alphas)
        dests = ''.join([alphas[rotation:], alphas[:rotation]])
        lookup |= {s: d for s, d in zip(alphas, dests)}
        return lookup

    def _processDefinition(self, line):
        # print(line)
        match = re.findall(r"(\w+)", line)
        self.sectorID = int(match[-2])
        checksum = match[-1]
        self.nameEncoded = '-'.join(match[:-2])
        self.isValid = checksum == self._generateChecksum(''.join(match[:-2]))
        # print("match: {} : list(match): {}".format(match, list(match)))
        # print("name: {} : checksum: {}".format(self.nameEncrypted, checksum))


class RoomCheck:
    """
    This seems as if it should be abstracted to a base class for this and the triangles problems, at least.
    """
    def __init__(self):
        self.candidates = []
        self.valid = []

    def countValid(self):
        """
        :return: Number of valid candidates
        """
        return len(self.valid)
#
    def printValid(self):
        """
        :return: None
        """
        for r in self.valid:
            print("{}: {}".format(r.sectorID, r.name))

    def readFile(self, fileName):
        with open(fileName) as inFile:
            for line in inFile:
                candidate = Room(line)
                self.candidates.append(candidate)
                if candidate:
                    self.valid.append(candidate)

    def sum(self):
        return sum(self.valid)
