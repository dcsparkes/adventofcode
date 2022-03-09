"""
https://adventofcode.com/2021/day/8
"""

from sevensegment import sevensegment

if __name__ == '__main__':
    # logging.basicConfig(filename="../log/2021_d08.log", encoding='utf-8', level=logging.WARNING)
    fInput = "input2021_08a.txt"
    fTest = "test2021_08a.txt"

    task1 = sevensegment.countUniqueLengthDigits(fInput)
    print("Task 1: {}".format(task1))
    task2 = sevensegment.sumOutputs(fInput)
    print("Task 2: {}".format(task2))