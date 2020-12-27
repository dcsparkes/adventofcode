import bisect

def get_ints(fileName):
    with open(fileName) as inFile:
       for line in inFile:
           # print(line)
           yield int(line.strip())

def get_joltages(fileName):
    joltages = [0]
    for joltage in get_ints(fileName):
        bisect.insort(joltages, joltage)
    joltages.append(joltages[-1] + 3)
    return joltages

def task1(fileName):
    return calc_joltage_checksum(get_joltages(fileName))

def task2(fileName):
    joltages = get_joltages(fileName)
    permutations = [1] + [0] * joltages[-1]
    for i in joltages[:-1]:
        pathCount = permutations[i]
        for k in range(1,4):
            permutations[i+k] += pathCount
    return permutations[-1]


def calc_joltage_checksum(joltages):
    diffs = [x - y for x, y in zip(joltages[1:],joltages[:-1])]
    return diffs.count(1) * diffs.count(3)

if __name__ == '__main__':
    print(get_joltages("test2020_10a.txt"))