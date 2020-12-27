import unittest
from indexedlinkedlist import indexedlinkedlist
from _2020 import d23_cupgame


class TestCupGame(unittest.TestCase):
    """
    Test the reimplementation of the functions for part one of: https://adventofcode.com/2020/day/23
    """

    def test_move_sequential(self):
        pattern = "389125467"
        expecteds = ["289154673", "546789132", "891346725", "467913258", "136792584", "936725841", "258367419",
                     "674158392", "574183926", "837419265"]
        ill = indexedlinkedlist.IndexedList(pattern)
        for e in expecteds:
            d23_cupgame.move(ill)
            self.assertEqual([int(c) for c in e], [val for val in ill])

    def test_move_1(self):
        pattern = "389125467"
        l = indexedlinkedlist.IndexedList(pattern)
        d23_cupgame.move(l)
        self.assertEqual([int(c) for c in "289154673"], [val for val in l])

    def test_move_2(self):
        pattern = "289154673"
        l = indexedlinkedlist.IndexedList(pattern)
        d23_cupgame.move(l)
        self.assertEqual([int(c) for c in "546789132"], [val for val in l])

    def test_move_3(self):
        pattern = "546789132"
        l = indexedlinkedlist.IndexedList(pattern)
        d23_cupgame.move(l)
        self.assertEqual([int(c) for c in "891346725"], [val for val in l])

    def test_move_4(self):
        pattern = "891346725"
        l = indexedlinkedlist.IndexedList(pattern)
        d23_cupgame.move(l)
        self.assertEqual([int(c) for c in "467913258"], [val for val in l])

    def test_move_5(self):
        pattern = "467913258"
        l = indexedlinkedlist.IndexedList(pattern)
        d23_cupgame.move(l)
        self.assertEqual([int(c) for c in "136792584"], [val for val in l])

    def test_move_6(self):
        pattern = "136792584"
        l = indexedlinkedlist.IndexedList(pattern)
        d23_cupgame.move(l)
        self.assertEqual([int(c) for c in "936725841"], [val for val in l])

    def test_move_7(self):
        pattern = "936725841"
        l = indexedlinkedlist.IndexedList(pattern)
        d23_cupgame.move(l)
        self.assertEqual([int(c) for c in "258367419"], [val for val in l])

    def test_move_8(self):
        pattern = "258367419"
        l = indexedlinkedlist.IndexedList(pattern)
        d23_cupgame.move(l)
        self.assertEqual([int(c) for c in "674158392"], [val for val in l])

    def test_move_9(self):
        pattern = "674158392"
        l = indexedlinkedlist.IndexedList(pattern)
        d23_cupgame.move(l)
        self.assertEqual([int(c) for c in "574183926"], [val for val in l])

    def test_move_10(self):
        pattern = "574183926"
        l = indexedlinkedlist.IndexedList(pattern)
        d23_cupgame.move(l)
        self.assertEqual([int(c) for c in "837419265"], [val for val in l])

    def test_playGame_sequential(self):
        pattern = "389125467"
        expecteds = ["54673289", "32546789", "34672589", "32584679", "36792584", "93672584", "92583674",
                     "58392674", "83926574", "92658374"]
        for i in range(len(expecteds)):
            expected = expecteds[i]
            report = d23_cupgame.playGame("389125467", i + 1)
            self.assertEqual([int(c) for c in expected], report, "i = {}".format(i))

    def test_playGame_test_0(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 0)])
        self.assertEqual("25467389", result)

    def test_playGame_test_1(self):
        initState = [int(c) for c in "389125467"]
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 1)])
        self.assertEqual("54673289", result)

    def test_playGame_test_2(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 2)])
        self.assertEqual("32546789", result)

    def test_playGame_test_3(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 3)])
        self.assertEqual("34672589", result)

    def test_playGame_test_4(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 4)])
        self.assertEqual("32584679", result)

    def test_playGame_test_5(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 5)])
        self.assertEqual("36792584", result)

    def test_playGame_test_6(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 6)])
        self.assertEqual("93672584", result)

    def test_playGame_test_7(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 7)])
        self.assertEqual("92583674", result)

    def test_playGame_test_8(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 8)])
        self.assertEqual("58392674", result)

    def test_playGame_test_9(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 9)])
        self.assertEqual("83926574", result)

    def test_playGame_test_10(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 10)])
        self.assertEqual("92658374", result)

    def test_playGame_test_100(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("389125467", 100)])
        self.assertEqual("67384529", result)

    def test_playGame_unknown_100(self):
        result = ''.join([str(n) for n in d23_cupgame.playGame("653427918", 100)])
        self.assertEqual("76952348", result)

    def test_playTenMillion_test(self):
        result = d23_cupgame.playTenMillion("389125467")
        self.assertEqual(149245887792, result)

    def test_playTenMillion_unknown(self):
        result = d23_cupgame.playTenMillion("653427918")
        self.assertEqual(None, result)

    def test_fullReport_known(self):
        patterns = [("389125467", "25467389"), ("837419265", "92658374"), ("12345", "2345")]
        for pattern, expected in patterns:
            ill = indexedlinkedlist.IndexedList(pattern)
            self.assertEqual([int(c) for c in expected], d23_cupgame.report(ill))

    def test_partialReport_known(self):
        patterns = [("389125467", "25467389"), ("837419265", "92658374"), ("12345", "2345")]
        for pattern, expected in patterns:
            ill = indexedlinkedlist.IndexedList(pattern)

            self.assertEqual(int(expected[0]) * int(expected[1]), d23_cupgame.report(ill, full=False))


class TestIndexedList(unittest.TestCase):
    def test_init_overPatterned(self):
        pattern = "389125467"
        size = 5
        with self.assertRaises(ValueError):
            indexedlinkedlist.IndexedList(pattern, size)

    def test_iter_fullPatterned_list(self):
        pattern = "389125467"
        l = indexedlinkedlist.IndexedList(pattern)
        expectedValues = [int(c) for c in pattern]
        listValues = [val for val in l]
        self.assertEqual(expectedValues, listValues)

    def test_iter_partiallyPatterned_10(self):
        pattern = "389125467"
        size = 10
        l = indexedlinkedlist.IndexedList(pattern, size)
        expectedValues = [int(c) for c in pattern]
        expectedValues.extend([i + 1 for i in range(len(pattern), size)])
        listValues = [val for val in l]
        self.assertEqual(expectedValues, listValues)

    def test_iter_partiallyPatterned_20(self):
        pattern = "389125467"
        size = 20
        l = indexedlinkedlist.IndexedList(pattern, size)
        expectedValues = [int(c) for c in pattern]
        expectedValues.extend([i + 1 for i in range(len(pattern), size)])
        listValues = [val for val in l]
        self.assertEqual(expectedValues, listValues)

    def test_iter_unpatterned_list(self):
        size = 6
        l = indexedlinkedlist.IndexedList(size=size)
        expectedValues = [i for i in range(1, size + 1)]
        listValues = [val for val in l]
        self.assertEqual(expectedValues, listValues)

    def test_iter_unpatterned_perItem(self):
        size = 6
        l = indexedlinkedlist.IndexedList(size=size)
        expectedValue = 1
        for value in l:
            self.assertEqual(expectedValue, value, expectedValue)
            expectedValue += 1

    def test_len_removeSliceReAdd_fullyPatterned(self):
        """
        Mirror the slice functions in a fully patterned list.
        :return:
        """
        pattern = "389125467"
        insertionPoint = 7
        ill = indexedlinkedlist.IndexedList(pattern)
        self.assertEqual(len(pattern), len(ill), "List init Mismatch: Test Aborted.")

        slice = ill.popSlice(1, 4)
        listSlice = [i for i in slice]
        self.assertEqual(3, len(listSlice), "Popped slice Mismatch: Test Aborted.")
        self.assertEqual(len(pattern) - 3, len(ill), "Remainder List Mismatch: Test Aborted.")

        ill.insertAfterValue(insertionPoint, slice)
        self.assertEqual(len(pattern), len(ill))

    def test_len_insertAfterValue_partiallyPatterned_20(self):
        """
        Mirror the slice functions in a partially patterned list.
        :return:
        """
        pattern = "389125467"
        size = 20
        insertionPoint = 13

        ill = indexedlinkedlist.IndexedList(pattern, size)

        self.assertEqual(size, len(ill), "List init Mismatch: Test Aborted.")

        slice = ill.popSlice(1, 4)
        listSlice = [i for i in slice]
        self.assertEqual(3, len(listSlice), "Popped slice Mismatch: Test Aborted.")
        self.assertEqual(size - 3, len(ill), "Remainder List Mismatch: Test Aborted.")

        ill.insertAfterValue(insertionPoint, slice)
        self.assertEqual(size, len(ill))

    def test_len_insertAfterValue_unpatterned_calculated(self):
        """
        Mirror the slice functions in a regular list.
        :return:
        """
        size = 10
        insertionPoint = 8
        ill = indexedlinkedlist.IndexedList(size=size)
        self.assertEqual(size, len(ill), "List init Mismatch: Test Aborted.")

        slice = ill.popSlice(1, 4)
        listSlice = [i for i in slice]
        self.assertEqual(3, len(listSlice), "Popped slice Mismatch: Test Aborted.")
        self.assertEqual(size - 3, len(ill), "Remainder List Mismatch: Test Aborted.")

        ill.insertAfterValue(insertionPoint, slice)
        self.assertEqual(size, len(ill))

    def test_indexing_fullPatterned(self):
        pattern = "389125467"
        l = indexedlinkedlist.IndexedList(pattern)
        for i in range(len(pattern)):
            self.assertEqual(int(pattern[i]), l[i], "Index = {}".format(i))

    def test_indexing_fullPatterned_0(self):
        l = indexedlinkedlist.IndexedList("389125467")
        self.assertEqual(3, l[0])

    def test_indexing_fullPatterned_1(self):
        l = indexedlinkedlist.IndexedList("389125467")
        self.assertEqual(8, l[1])

    def test_indexing_fullPatterned_2(self):
        l = indexedlinkedlist.IndexedList("389125467")
        self.assertEqual(9, l[2])

    def test_indexing_fullPatterned_3(self):
        l = indexedlinkedlist.IndexedList("389125467")
        self.assertEqual(1, l[3])

    def test_indexing_fullPatterned_4(self):
        l = indexedlinkedlist.IndexedList("389125467")
        self.assertEqual(2, l[4])

    def test_indexing_fullPatterned_5(self):
        l = indexedlinkedlist.IndexedList("389125467")
        self.assertEqual(5, l[5])

    def test_indexing_fullPatterned_6(self):
        l = indexedlinkedlist.IndexedList("389125467")
        self.assertEqual(4, l[6])

    def test_indexing_fullPatterned_7(self):
        l = indexedlinkedlist.IndexedList("389125467")
        self.assertEqual(6, l[7])

    def test_indexing_fullPatterned_8(self):
        l = indexedlinkedlist.IndexedList("389125467")
        self.assertEqual(7, l[8])

    def test_indexing_fullPatterned_9(self):
        l = indexedlinkedlist.IndexedList("389125467")
        self.assertEqual(3, l[9])

    def test_indexing_partiallyPatterned_10(self):
        pattern = "389125467"
        size = 10
        l = indexedlinkedlist.IndexedList(pattern, size)
        for i in range(len(pattern)):
            # print(i, end=': ')
            self.assertEqual(int(pattern[i]), l[i], "Index = {}".format(i))
        for i in range(len(pattern), size):
            # print(i, end=': ')
            self.assertEqual(i + 1, l[i], "Index = {}".format(i))

    def test_indexing_partiallyPatterned_20(self):
        pattern = "389125467"
        size = 20
        l = indexedlinkedlist.IndexedList(pattern, size)
        for i in range(len(pattern)):
            # print(i, end=': ')
            self.assertEqual(int(pattern[i]), l[i], "Index = {}".format(i))
        for i in range(len(pattern), size):
            # print(i, end=': ')
            self.assertEqual(i + 1, l[i], "Index = {}".format(i))

    def test_indexing_unpatterned_0(self):
        l = indexedlinkedlist.IndexedList(size=5)
        self.assertEqual(1, l[0])

    def test_indexing_unpatterned_1(self):
        l = indexedlinkedlist.IndexedList(size=5)
        self.assertEqual(2, l[1])

    def test_indexing_unpatterned_2(self):
        l = indexedlinkedlist.IndexedList(size=5)
        self.assertEqual(3, l[2])

    def test_indexing_unpatterned_3(self):
        l = indexedlinkedlist.IndexedList(size=5)
        self.assertEqual(4, l[3])

    def test_indexing_unpatterned_4(self):
        l = indexedlinkedlist.IndexedList(size=5)
        self.assertEqual(5, l[4])

    def test_indexing_unpatterned_5(self):
        l = indexedlinkedlist.IndexedList(size=5)
        self.assertEqual(1, l[5])

    def test_insertAfterValue_fullyPatterned(self):
        """
        Mirror the slice functions in a fully patterned list.
        :return:
        """
        pattern = "389125467"
        insertionPoint = 7
        l = indexedlinkedlist.IndexedList(pattern)
        expectedValues = [int(c) for c in pattern]
        listValues = [val for val in l]
        # print(expectedValues)
        self.assertEqual(expectedValues, [val for val in l], "List init Mismatch: Test Aborted.")

        slice = l.popSlice(1, 4)
        listSlice = [i for i in slice]
        expectedSlice = expectedValues[1:4]
        # print(expectedSlice)
        self.assertEqual(expectedSlice, listSlice, "Popped slice Mismatch: Test Aborted.")

        expectedValues = expectedValues[:1] + expectedValues[4:]
        # print(expectedValues)
        self.assertEqual(expectedValues, [val for val in l], "Remainder List Mismatch: Test Aborted.")

        index = expectedValues.index(insertionPoint)
        expectedValues = expectedValues[:index + 1] + expectedSlice + expectedValues[index + 1:]
        # print(expectedValues)
        l.insertAfterValue(insertionPoint, slice)
        self.assertEqual(expectedValues, [val for val in l])

    def test_insertAfterValue_partiallyPatterned_20(self):
        """
        Mirror the slice functions in a partially patterned list.
        :return:
        """
        pattern = "389125467"
        size = 20
        insertionPoint = 13

        l = indexedlinkedlist.IndexedList(pattern, size)
        expectedValues = [int(c) for c in pattern]
        expectedValues.extend([i + 1 for i in range(len(pattern), size)])
        # print(expectedValues)
        self.assertEqual(expectedValues, [val for val in l], "List init Mismatch: Test Aborted.")

        slice = l.popSlice(1, 4)
        listSlice = [i for i in slice]
        expectedSlice = expectedValues[1:4]
        # print(expectedSlice)
        self.assertEqual(expectedSlice, listSlice, "Popped slice Mismatch: Test Aborted.")

        expectedValues = expectedValues[:1] + expectedValues[4:]
        # print(expectedValues)
        self.assertEqual(expectedValues, [val for val in l], "Remainder List Mismatch: Test Aborted.")

        index = expectedValues.index(insertionPoint)
        expectedValues = expectedValues[:index + 1] + expectedSlice + expectedValues[index + 1:]
        # print(expectedValues)
        l.insertAfterValue(insertionPoint, slice)
        self.assertEqual(expectedValues, [val for val in l])

    def test_insertAfterValue_unpatterned_calculated(self):
        """
        Mirror the slice functions in a regular list.
        :return:
        """
        size = 10
        l = indexedlinkedlist.IndexedList(size=size)
        sortedValues = [i for i in range(1, size + 1)]
        self.assertEqual(sortedValues, [val for val in l], "List init Mismatch: Test Aborted.")

        slice = l.popSlice(1, 4)
        listSlice = [i for i in slice]
        expectedSlice = sortedValues[1:4]
        self.assertEqual(expectedSlice, listSlice, "Popped slice Mismatch: Test Aborted.")

        expectedValues = sortedValues[:1] + sortedValues[4:]
        self.assertEqual(expectedValues, [val for val in l], "Remainder List Mismatch: Test Aborted.")

        index = expectedValues.index(7)
        expectedValues = expectedValues[:index + 1] + expectedSlice + expectedValues[index + 1:]
        l.insertAfterValue(7, slice)
        self.assertEqual(expectedValues, [val for val in l])

    def test_insertAfterValue_unpatterned_fixed(self):
        size = 7
        l = indexedlinkedlist.IndexedList(size=size)
        sortedValues = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(sortedValues, [val for val in l], "List init Mismatch: Test Aborted.")
        slice = l.popSlice(1, 4)
        listSlice = [i for i in slice]
        expectedSlice = [2, 3, 4]
        self.assertEqual(expectedSlice, listSlice, "Popped slice Mismatch: Test Aborted.")
        expectedValues = [1, 5, 6, 7]
        self.assertEqual(expectedValues, [val for val in l], "Remainder List Mismatch: Test Aborted.")
        expectedValues = [1, 5, 6, 2, 3, 4, 7]
        l.insertAfterValue(6, slice)
        self.assertEqual(expectedValues, [val for val in l])

    def test_popSlice_isPopped(self):
        l = indexedlinkedlist.IndexedList(size=5)
        slice = l.popSlice(1, 4)
        self.assertEqual(1, l[0])
        self.assertEqual(5, l[1])

    def test_popSlice_checkLengthOfList(self):
        l = indexedlinkedlist.IndexedList(size=5)
        self.assertEqual(5, len(l))
        slice = l.popSlice(1, 4)
        self.assertEqual(2, len(l))

    def test_popSlice_checkLengthOfSlice_byInspection(self):
        ill = indexedlinkedlist.IndexedList(size=5)
        slice = ill.popSlice(1, 4)
        item = slice.nextItem
        length = 1
        while item is not None and item is not slice:
            item = item.nextItem
            length += 1
        self.assertEqual(3, length)

    def test_popSlice_checkLengthOfSlice_byLenFunction(self):
        ill = indexedlinkedlist.IndexedList(size=5)
        slice = ill.popSlice(1, 4)
        self.assertEqual(3, len(slice))

    def test_popSlice_checkLengthOfSlice_byListConversion(self):
        ill = indexedlinkedlist.IndexedList(size=5)
        slice = ill.popSlice(1, 4)
        self.assertEqual(3, len([val for val in slice]))

    def test_popSlice_checkSlice(self):
        l = indexedlinkedlist.IndexedList(size=5)
        slice = l.popSlice(1, 4)
        poppedList = [i for i in slice]
        self.assertEqual([2, 3, 4], poppedList)

    def test_popSlice_contains(self):
        l = indexedlinkedlist.IndexedList(size=5)
        slice = l.popSlice(1, 4)
        poppedList = [i for i in slice]
        self.assertEqual([2, 3, 4], poppedList)

    def test_popSlice_sliceContainsHead(self):
        l = indexedlinkedlist.IndexedList(size=6)
        slice = l.popSlice(4, 8)
        poppedList = [i for i in slice]
        remainingList = [i for i in l]
        self.assertEqual([5, 6, 1, 2], poppedList)
        self.assertEqual([4, 3], remainingList)

    def test_rotate_default(self):
        l = indexedlinkedlist.IndexedList(size=7)
        l.rotate()
        self.assertEqual([2, 3, 4, 5, 6, 7, 1], [val for val in l])

    def test_rotate_default(self):
        l = indexedlinkedlist.IndexedList(size=7)
        l.rotate(-1)
        self.assertEqual([7, 1, 2, 3, 4, 5, 6], [val for val in l])

    def test_rotate_listSize(self):
        l = indexedlinkedlist.IndexedList(size=7)
        l.rotate(7)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], [val for val in l])

    def test_rotate_listSizePlusOne(self):
        l = indexedlinkedlist.IndexedList(size=7)
        l.rotate(8)
        self.assertEqual([2, 3, 4, 5, 6, 7, 1], [val for val in l])


class TestCupGameTestFunctions(unittest.TestCase):
    """
    Test the original functions for part one of: https://adventofcode.com/2020/day/23
    These may be used to test the reimplemented functions
    """

    def test_move_1(self):
        initState = [int(c) for c in "389125467"]
        nextState = OldFunctions.move(initState)
        self.assertEqual([int(c) for c in "289154673"], nextState)

    def test_move_2(self):
        initState = [int(c) for c in "289154673"]
        nextState = OldFunctions.move(initState)
        self.assertEqual([int(c) for c in "546789132"], nextState)

    def test_move_3(self):
        initState = [int(c) for c in "546789132"]
        nextState = OldFunctions.move(initState)
        self.assertEqual([int(c) for c in "891346725"], nextState)

    def test_move_4(self):
        initState = [int(c) for c in "891346725"]
        nextState = OldFunctions.move(initState)
        self.assertEqual([int(c) for c in "467913258"], nextState)

    def test_move_5(self):
        initState = [int(c) for c in "467913258"]
        nextState = OldFunctions.move(initState)
        self.assertEqual([int(c) for c in "136792584"], nextState)

    def test_move_6(self):
        initState = [int(c) for c in "136792584"]
        nextState = OldFunctions.move(initState)
        self.assertEqual([int(c) for c in "936725841"], nextState)

    def test_move_7(self):
        initState = [int(c) for c in "936725841"]
        nextState = OldFunctions.move(initState)
        self.assertEqual([int(c) for c in "258367419"], nextState)

    def test_move_8(self):
        initState = [int(c) for c in "258367419"]
        nextState = OldFunctions.move(initState)
        self.assertEqual([int(c) for c in "674158392"], nextState)

    def test_move_9(self):
        initState = [int(c) for c in "674158392"]
        nextState = OldFunctions.move(initState)
        self.assertEqual([int(c) for c in "574183926"], nextState)

    def test_move_10(self):
        initState = [int(c) for c in "574183926"]
        nextState = OldFunctions.move(initState)
        self.assertEqual([int(c) for c in "837419265"], nextState)

    def test_playGame_test_10(self):
        initState = [int(c) for c in "389125467"]
        result = ''.join([str(n) for n in OldFunctions.playGame(initState, 10)])
        self.assertEqual("92658374", result)

    def test_playGame_test_100(self):
        initState = [int(c) for c in "389125467"]
        result = ''.join([str(n) for n in OldFunctions.playGame(initState, 100)])
        self.assertEqual("67384529", result)

    def test_playGame_unknown_100(self):
        initState = [int(c) for c in "653427918"]
        result = ''.join([str(n) for n in OldFunctions.playGame(initState, 100)])
        self.assertEqual("76952348", result)

    def test_report_known(self):
        initState = [int(c) for c in "837419265"]
        self.assertEqual([int(c) for c in "92658374"], OldFunctions.report(initState))


class OldFunctions:
    @staticmethod
    def move(input):
        input = [int(c) for c in input]
        maxInput = max(input)
        inputLen = len(input)

        claw = input[1:4]
        circle = input[4:] + input[:1]
        selection = input[0] - 1
        # print(selection, end=', ')
        while selection not in circle:
            if not selection:
                selection = selection + inputLen
            else:
                selection -= 1
            # print(selection, end=', ')
        # print("\ninput: {}, max: {}, claw: {}, circle: {}, selection: {}".format(input, maxInput, claw, circle, selection))
        index = circle.index(selection)
        newArrangement = circle[:index + 1] + claw + circle[index + 1:]
        # print(newArrangement)
        return newArrangement

    @staticmethod
    def playGame(input, iterations, fullReport=True):
        arrangement = input
        for i in range(iterations):
            arrangement = OldFunctions.move(arrangement)

        return OldFunctions.report(arrangement)

    @staticmethod
    def report(input, full=True):
        index = input.index(1)
        if not full:
            length = len(input)
            return input[(index + 1) % length] * input[(index + 2) % length]
        else:
            return input[index + 1:] + input[:index]


if __name__ == '__main__':
    unittest.main()
