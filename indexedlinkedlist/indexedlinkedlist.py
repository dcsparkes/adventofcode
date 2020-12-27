"""
Indexed Linked List for part two of: https://adventofcode.com/2020/day/23
Index is to make the deletions and insertions O(1)

NotTested: What happens if you pop the head?
"""


class IndexedList():
    def __init__(self, pattern="", size=None):
        """
        Reimplement to be lazy? Not relevant for this application
        :param pattern:
        :param size: length of list.  If None assume length of pattern.
        """
        if not size:
            self.size = len(pattern)
        else:
            self.size = size
        self.length = self.size
        self.listIndex = [ListItem(i + 1) for i in range(self.size)]
        if pattern:
            if self.size < len(pattern):
                raise ValueError("{}: Size cannot be less than pattern length.".format(self.__class__.__name__))
            maxAllocated, tailTip = self._readPattern(pattern)
        else:
            self.head = self.listIndex[0]
            self.head.nextItem = self.head

            tailTip = 0
            maxAllocated = 1

        if maxAllocated < self.size:
            self.listIndex[-1].nextItem = self.head
            self.listIndex[tailTip].nextItem = self.listIndex[maxAllocated]
            for i in range(maxAllocated, self.size - 1):
                self.listIndex[i].nextItem = self.listIndex[i + 1]

    def __getitem__(self, key):
        item = self.head
        for i in range(int(key) % self.size):
            # print(item, end=', ')
            item = item.nextItem
        # print(item)
        return item.value

    def __iter__(self):
        for item in self.head:
            yield item

    def __len__(self):
        return self.length

    def _readPattern(self, pattern):
        """
        For now assume no holes in the pattern.  Holes are not filled.
        :param pattern: list of the order of the linked list
        :return: maximum allocated value
        """
        values = [int(c) for c in pattern]
        prev = None
        for c in values:
            if prev:
                self.listIndex[prev - 1].nextItem = self.listIndex[c - 1]
            else:
                self.listIndex[-1].nextItem = self.listIndex[c - 1]
                self.head = self.listIndex[c - 1]
            prev = c
        self.listIndex[c - 1].nextItem = self.head
        return max(values), c - 1

    def insertAfterValue(self, value, listFragment):
        fragLen = 0
        ptrPos = self.listIndex[value - 1]
        ptrNext = ptrPos.nextItem
        ptrPos.nextItem = listFragment
        while ptrPos.nextItem is not None:
            ptrPos = ptrPos.nextItem
            fragLen += 1
        ptrPos.nextItem = ptrNext
        self.length += fragLen

    def popSlice(self, start, end):
        """
        Pop the slice as if it were a list
        :param start: start index of circular list
        :param end: end index of circular list
        :return: None terminated linked list. i.e. First item of slice
        """
        if end < start:
            raise ValueError("End before start.")
        elif end - start > len(self) - 1:
            raise ValueError("Range {}-{} would include entire list".format(start, end))  # Could rotate(start) and return entire list.  Would need to signal empty original.

        prevPtr = self.head
        startPtr = self.head.nextItem

        for _ in range(start - 1):
            # print(startPtr, end=', ')
            prevPtr = startPtr
            startPtr = startPtr.nextItem

        endPtr = startPtr
        rangeContainsHead = startPtr == self.head

        for _ in range(start, end - 1):
            endPtr = endPtr.nextItem
            rangeContainsHead |= endPtr == self.head

        prevPtr.nextItem = endPtr.nextItem  # Cut out slice
        self.length -= (end - start)

        if rangeContainsHead:
            self.head = prevPtr  # .nextItem ??  Move head before break or after?  TBD
        endPtr.nextItem = None  # Terminate slice
        assert len(startPtr) == (end - start)
        return startPtr

    def rotate(self, inc=1):
        for i in range(inc % len(self)):
            self.head = self.head.nextItem

    def rotateToOne(self, inc=1):
        self.head = self.listIndex[0]


class ListItem():
    def __init__(self, value, nextItem=None):
        # self.index = ListIndex()
        self.value = value
        self.linkTo(nextItem)

    def __iter__(self):
        yield self.value
        current = self.nextItem
        while current is not None and current is not self:
            yield current.value
            current = current.nextItem

    def __len__(self):
        # return 1
        retVal = 1
        item = self.nextItem
        while item is not None and item is not self:
            item = item.nextItem
            retVal += 1
        return retVal

    def __repr__(self):
        return "{}({} -> {})".format(self.__class__.__name__, self.value,
                                     self.nextItem.value if self.nextItem else self.nextItem)

    def linkTo(self, nextItem=None):
        if nextItem is None or type(nextItem) is ListItem:
            self.nextItem = nextItem
        else:
            self.nextItem = None  # self.index(nextItem)
