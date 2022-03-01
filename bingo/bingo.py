"""
https://adventofcode.com/2021/day/4
"""
from base import base


class Card:
    def __init__(self, numbers):
        self.grid = numbers

    @staticmethod
    def _winlines(grid):
        """
        Given a grid of either numbers or durations, yield every possible winning line.  Diagonals not included but
        relatively easy to extend functionality.

        :param grid: a grid of either numbers or durations
        :return: every possible winning line
        """
        for row in grid:  # rows
            yield tuple(row)

        for column in zip(*grid):  # columns
            yield column

    def _winDuration(self, grid):
        """
        Given a grid of durations, yield the duration of every line that wins.

        :param grid:
        :return:
        """
        for line in self._winlines(grid):
            if None not in line:  # Exclude non-winning lines
                yield max(line)

    def calculateWinMoves(self, sequence):
        """
        Calculate how many moves it takes to win with this card.

        :param sequence: Bingo numbers drawn, in order
        :return:
        """
        durations = [[sequence.index(n) if n in sequence else None for n in row] for row in self.grid]
        return 1 + min(self._winDuration(durations))

    def calculateScore(self, sequence):
        """
        Calculate the sum of the remaining numbers on the card after the sequence has been played.  It is assumed that
        the sequence has been truncated to the length calculated by calculateWinMoves().

        :param sequence: Bingo numbers drawn, in order
        :return: Score = remainder * final move
        """
        remainder = sum([int(n) for row in self.grid for n in row if n not in sequence])
        return remainder * int(sequence[-1])


class Game:
    def __init__(self, fileName):
        self.cards = []
        self.sequence = []
        currentCard = []
        for line in base.getInputLines(fileName):
            if ',' in line:
                self.sequence.extend(line.split(','))

            elif not line:
                if currentCard:
                    self.addCard(currentCard)
                    currentCard = []

            else:
                currentCard.append(line.split())

        if currentCard:
            self.addCard(currentCard)

    def addCard(self, numbers):
        self.cards.append(Card(numbers))

    def playSequence(self, sequence=None):
        """
        Plays through the sequence.

        :param sequence: Inject a different sequence (mainly anticipated for test purposes)
        :return: tuple of winner index and move count
        """
        if sequence is None:
            sequence = self.sequence

        winMoves = [c.calculateWinMoves(sequence) for c in self.cards]
        winnerMoves = min(winMoves)
        loserMoves = max(winMoves)
        winner = winMoves.index(winnerMoves)
        loser = winMoves.index(loserMoves)
        winScore = self.cards[winner].calculateScore(sequence[:winnerMoves])
        loseScore = self.cards[loser].calculateScore(sequence[:loserMoves])
        return ((winner, winnerMoves, winScore), (loser, loserMoves, loseScore))
