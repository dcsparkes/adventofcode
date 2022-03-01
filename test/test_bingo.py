"""
https://adventofcode.com/2021/day/4
"""
import unittest

from bingo import bingo


class testBingoCard(unittest.TestCase):
    incrementingPattern = [['1', '2', '3', '4', '5'],
                           ['6', '7', '8', '9', '10'],
                           ['11', '12', '13', '14', '15'],
                           ['16', '17', '18', '19', '20'],
                           ['21', '22', '23', '24', '25']
                           ]

    def test_calculateWinMoves_simpleColumnCount(self):
        card = bingo.Card(self.incrementingPattern)
        for row in card.grid:
            self.assertEqual(5, len(row))

    def test_calculateWinMoves_simpleRowCount(self):
        card = bingo.Card(self.incrementingPattern)
        self.assertEqual(5, len(card.grid))

    def test_calculateWinMoves_worstCase1(self):
        card = bingo.Card(self.incrementingPattern)
        moves = card.calculateWinMoves(['2', '3', '4', '5',
                                        '6', '8', '9', '10',
                                        '11', '12', '14', '15',
                                        '16', '17', '18', '20',
                                        '21', '22', '23', '24',
                                        '1', '7', '13', '19', '25'])
        self.assertEqual(21, moves)

    def test_calculateWinMoves_worstCase2(self):
        card = bingo.Card(self.incrementingPattern)
        moves = card.calculateWinMoves(['2', '3', '4', '5',
                                        '6', '8', '9', '10',
                                        '11', '12', '14', '15',
                                        '16', '17', '18', '20',
                                        '21', '22', '23', '24',
                                        '7', '13', '19', '25', '1'])
        self.assertEqual(21, moves)

    def test_calculateWinMoves_worstCase3(self):
        card = bingo.Card(self.incrementingPattern)
        moves = card.calculateWinMoves(['2', '3', '4', '5',
                                        '6', '8', '9', '10',
                                        '11', '12', '14', '15',
                                        '16', '17', '18', '20',
                                        '21', '22', '23', '24',
                                        '13', '19', '25', '1', '7'])
        self.assertEqual(21, moves)

    def test_calculateWinMoves_worstCase4(self):
        card = bingo.Card(self.incrementingPattern)
        moves = card.calculateWinMoves(['2', '3', '4', '5',
                                        '6', '8', '9', '10',
                                        '11', '12', '14', '15',
                                        '16', '17', '18', '20',
                                        '21', '22', '23', '24',
                                        '19', '25', '1', '7', '13'])
        self.assertEqual(21, moves)

    def test_calculateWinMoves_worstCase5(self):
        card = bingo.Card(self.incrementingPattern)
        moves = card.calculateWinMoves(['2', '3', '4', '5',
                                        '6', '8', '9', '10',
                                        '11', '12', '14', '15',
                                        '16', '17', '18', '20',
                                        '21', '22', '23', '24',
                                        '25', '1', '7', '13', '19'])
        self.assertEqual(21, moves)

    def test_calculateWinMoves_simpleHorizontal(self):
        card = bingo.Card(self.incrementingPattern)
        moves = card.calculateWinMoves(['1', '2', '3', '4', '5', '6'])
        self.assertEqual(5, moves)

    def test_calculateWinMoves_simpleVertical(self):
        card = bingo.Card(self.incrementingPattern)
        moves = card.calculateWinMoves(['1', '6', '11', '16', '21', '25'])
        self.assertEqual(5, moves)

    def test__winLines_incrementing(self):
        card = bingo.Card(self.incrementingPattern)

        lines = card._winlines(self.incrementingPattern)
        self.assertEqual(('1', '2', '3', '4', '5'), next(lines))
        self.assertEqual(('6', '7', '8', '9', '10'), next(lines))
        self.assertEqual(('11', '12', '13', '14', '15'), next(lines))
        self.assertEqual(('16', '17', '18', '19', '20'), next(lines))
        self.assertEqual(('21', '22', '23', '24', '25'), next(lines))
        self.assertEqual(('1', '6', '11', '16', '21'), next(lines))
        self.assertEqual(('2', '7', '12', '17', '22'), next(lines))
        self.assertEqual(('3', '8', '13', '18', '23'), next(lines))
        self.assertEqual(('4', '9', '14', '19', '24'), next(lines))
        self.assertEqual(('5', '10', '15', '20', '25'), next(lines))
        with self.assertRaises(StopIteration):
            next(lines)


class testBingoGame(unittest.TestCase):
    fInput = "input2021_04a.txt"
    fTest = "test2021_04a.txt"

    def test_cardCount_fInput(self):
        game = bingo.Game(self.fInput)
        self.assertEqual(100, len(game.cards))

    def test_cardCount_fTest(self):
        game = bingo.Game(self.fTest)
        self.assertEqual(3, len(game.cards))

    def test_sequenceLength_fInput(self):
        game = bingo.Game(self.fInput)
        self.assertEqual(100, len(game.sequence))

    def test_sequenceLength_fTest(self):
        game = bingo.Game(self.fTest)
        self.assertEqual(27, len(game.sequence))

    def test_sequenceMaximum_fInput(self):
        game = bingo.Game(self.fInput)
        self.assertEqual(99, max([int(x) for x in game.sequence]))

    def test_sequenceMaximum_fTest(self):
        game = bingo.Game(self.fTest)
        self.assertEqual(26, max([int(x) for x in game.sequence]))

    def test_loseMoveCount_fInput(self):
        game = bingo.Game(self.fInput)
        winStats, loseStats = game.playSequence()
        self.assertEqual(88, loseStats[1])

    def test_loseMoveCount_fTest(self):
        game = bingo.Game(self.fTest)
        winStats, loseStats = game.playSequence()
        self.assertEqual(15, loseStats[1])

    def test_loser_fInput(self):
        game = bingo.Game(self.fInput)
        winStats, loseStats = game.playSequence()
        self.assertEqual(28, loseStats[0])

    def test_loser_fTest(self):
        game = bingo.Game(self.fTest)
        winStats, loseStats = game.playSequence()
        self.assertEqual(1, loseStats[0])

    def test_loseScore_fInput(self):
        game = bingo.Game(self.fInput)
        winStats, loseStats = game.playSequence()
        self.assertEqual(17884, loseStats[2])

    def test_loseScore_fTest(self):
        game = bingo.Game(self.fTest)
        winStats, loseStats = game.playSequence()
        self.assertEqual(1924, loseStats[2])

    def test_winMoveCount_fInput(self):
        game = bingo.Game(self.fInput)
        winStats, loseStats = game.playSequence()
        self.assertEqual(19, winStats[1])

    def test_winMoveCount_fTest(self):
        game = bingo.Game(self.fTest)
        winStats, loseStats = game.playSequence()
        self.assertEqual(12, winStats[1])

    def test_winner_fInput(self):
        game = bingo.Game(self.fInput)
        winStats, loseStats = game.playSequence()
        self.assertEqual(89, winStats[0])

    def test_winner_fTest(self):
        game = bingo.Game(self.fTest)
        winStats, loseStats = game.playSequence()
        self.assertEqual(2, winStats[0])

    def test_winScore_fInput(self):
        game = bingo.Game(self.fInput)
        winStats, loseStats = game.playSequence()
        self.assertEqual(74320, winStats[2])

    def test_winScore_fTest(self):
        game = bingo.Game(self.fTest)
        winStats, loseStats = game.playSequence()
        self.assertEqual(4512, winStats[2])


if __name__ == '__main__':
    unittest.main()
