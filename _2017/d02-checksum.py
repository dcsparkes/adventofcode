from base import base


def checksumFromFile(fileName):
    total = 0
    for row in base.getInputLines(fileName):
        entries = [int(e) for e in row.split('\t')]
        total += max(entries) - min(entries)
    return total


def findIntegerDivision(entries):
    """
    :param entries: sorted list
    :return: 
    """
    count = len(entries)
    print(entries)
    for i in range(count):
        for j in range(i + 1, count):
            if not entries[j] % entries[i]:
                print("{}//{}={}".format(entries[j], entries[i], entries[j] / entries[i]))
                return entries[j] // entries[i]


def factorsFromFile(fileName):
    total = 0
    for row in base.getInputLines(fileName):
        entries = sorted([int(e) for e in row.split('\t')])
        total += findIntegerDivision(entries)
    return total


if __name__ == '__main__':
    print("Task1: ", checksumFromFile("input2017_02a.txt"))
    print("Test:   ", factorsFromFile("test2017_02a.txt"))
    print("Task2: ", factorsFromFile("input2017_02a.txt"))

    # print(totalDiametricRepeats("1212"))
