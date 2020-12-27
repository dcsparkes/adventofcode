def openInput(fileName):
    with open(fileName) as inFile:
        for line in inFile:
            yield line.strip()


def findPair(total, fileName):
    """Find the first pair of numbers that insert up to total.
    Return pair as tuple."""

    counterparts = dict()
    total = int(total)
    for line in openInput(fileName):
        num = int(line)
        # print("Line {}: {}".format(num, total - num))
        if num in counterparts:
            return (counterparts[num], num)

        else:
            counterparts[total - num] = num


def findTriplet(total, fileName):
    """Find the first triplet of numbers that insert up to total.
    Assumptions: positive integers: i.e. no need to track totals larger than 2000.
    Return triplet as tuple."""
    import bisect

    entries = []
    counterparts = dict()
    total = int(total)

    if total < 1:
        raise(ValueError('Positive Integers only'))

    for line in openInput(fileName):
        entry = int(line)
        # print("Line {}: {}".format(entry, total - entry))
        # print(entries)
        # print(entry > total)
        # print(not entries)

        if entry > total:
            # Ignore any numbers greater than total.
            # More sophisticated might reject any number greater than total minus by 2 * min or the sum
            # of the two smallest numbers.  [O(n) to find min, but must load entire list.]
            pass

        elif not entries:
            # First number has nothing to be multiplied with.
            entries = [entry]

        elif entry in counterparts:
            # Solution found
            a, b = counterparts[entry]
            return (a, b, entry)

        else:
            # Populate counterpart pairs
            for i in entries:
                rem = total - (entry + i)
                if rem > 0:
                    counterparts[rem] = (i, entry)

            # Insert num in history list sorted
            bisect.insort(entries, entry)
    print(entries)
    return (0,0,0)