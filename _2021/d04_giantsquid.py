"""
https://adventofcode.com/2021/day/4
"""
from bingo import bingo

# import logging
# import sys

if __name__ == '__main__':
    # logging.basicConfig(filename="../log/2021_d05.log", encoding='utf-8', level=logging.WARNING)
    fInput = "input2021_04a.txt"
    game = bingo.Game(fInput)
    win, lose = game.playSequence()
    print("Winner: card {} in {} moves with a final score of {}.".format(*win))
    print("Loser: card {} in {} moves with a final score of {}.".format(*lose))
