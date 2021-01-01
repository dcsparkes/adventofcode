"""
https://adventofcode.com/2020/day/15
"""
import unittest


class MemoryGame:
    def __init__(self):
        self.memory = {}

    def say(self, number, turn):
        """
        :param current number:
        :return: next number
        """
        numNext = 0
        if number in self.memory:
            numNext = turn - self.memory[number]
        self.memory[number] = turn
        return numNext

    def play(self, stream, gameEnd=2020, outLoud=False):
        self.memory = {}
        turn = 0
        nextSaid = None

        for item in stream:
            turn += 1
            nextSaid = self.say(item, turn)

        while (turn < gameEnd - 1):
            turn += 1
            nextSaid = self.say(nextSaid, turn)

        if outLoud:
            print("{}th numbers: {}".format(gameEnd, nextSaid))
        return nextSaid

    def write(self, address, value, masks):
        self.mem[address] = self.applyMasks(masks, int(value))


class TestMemBank_v2(unittest.TestCase):
    gameInput = (240, 505, [14, 8, 16, 0, 1, 17])
    gameTest0 = (436, 175594, [0, 3, 6])
    gameTest1 = (1, 2578, [1, 3, 2])
    gameTest2 = (10, 3544142, [2, 1, 3])
    gameTest3 = (27, 261214, [1, 2, 3])
    gameTest4 = (78, 6895259, [2, 3, 1])
    gameTest5 = (438, 18, [3, 2, 1])
    gameTest6 = (1836, 362, [3, 1, 2])

    def test_MemoryGame_gameInput_2020(self):
        result2k2, result3e7, game = self.gameInput
        mg = MemoryGame()
        self.assertEqual(result2k2, mg.play(game, outLoud=True))

    def test_MemoryGame_gameInput_3e7(self):
        result2k2, result3e7, game = self.gameInput
        mg = MemoryGame()
        self.assertEqual(result3e7, mg.play(game, 3 * (10 ** 7), outLoud=True))

    def test_MemoryGame_gameTest0_2020(self):
        result2k2, result3e7, game = self.gameTest0
        mg = MemoryGame()
        self.assertEqual(result2k2, mg.play(game))

    def test_MemoryGame_gameTest1_2020(self):
        result2k2, result3e7, game = self.gameTest1
        mg = MemoryGame()
        self.assertEqual(result2k2, mg.play(game))

    def test_MemoryGame_gameTest2_2020(self):
        result2k2, result3e7, game = self.gameTest2
        mg = MemoryGame()
        self.assertEqual(result2k2, mg.play(game))

    def test_MemoryGame_gameTest3_2020(self):
        result2k2, result3e7, game = self.gameTest3
        mg = MemoryGame()
        self.assertEqual(result2k2, mg.play(game))

    def test_MemoryGame_gameTest4_2020(self):
        result2k2, result3e7, game = self.gameTest4
        mg = MemoryGame()
        self.assertEqual(result2k2, mg.play(game))

    def test_MemoryGame_gameTest5_2020(self):
        result2k2, result3e7, game = self.gameTest5
        mg = MemoryGame()
        self.assertEqual(result2k2, mg.play(game))

    def test_MemoryGame_gameTest6_2020(self):
        result2k2, result3e7, game = self.gameTest6
        mg = MemoryGame()
        self.assertEqual(result2k2, mg.play(game))


if __name__ == '__main__':
    unittest.main()
