"""
https://adventofcode.com/2020/day/22
"""
from base import base


def readHands(fileName):
    hand = []
    for line in base.getInputLines(fileName):
        # print(line)
        if not line:
            pass
        elif line[:6] == "Player":
            if hand:
                yield hand[::-1]
                hand.clear()
        else:
            # print(line)
            hand.append(int(line))
    yield hand[::-1]


def playGame(fileName):
    hands = [hand for hand in readHands(fileName)]
    # print(hands)
    while hands[0] and hands[1]:
        round = [hand.pop() for hand in hands]
        winner = round.index(max(round))
        hands[winner] = sorted(round) + hands[winner]
        # print(hands)

    return score(hands[winner])


def playRecursiveSubgame(hands, gameID):
    histories = [[], []]
    while hands[0] and hands[1]:
        # print("GAME {}: {}".format(gameID, hands), end ='')
        handLengths = []
        for i in range(len(hands)):
            if hands[i] in histories[i]:
                # print("\nLoop Detected: {} in {}".format(hands[i], histories[i]))
                return 0
            else:
                histories[i].append(hands[i][:])
                handLengths.append(len(hands[i]))

        round = [hand.pop() for hand in hands]
        # print(round)
        if False in [round[i] < handLengths[i] for i in range(len(round))]:
            winner = round.index(max(round))
        else:
            winner = playRecursiveSubgame([hands[i][-round[i]:] for i in range(len(round))], gameID + 1)

        hands[winner] = [round[1 - winner]] + [round[winner]] + hands[winner]
    return winner


def playRecursiveGame(fileName):
    hands = [hand for hand in readHands(fileName)]
    winner = playRecursiveSubgame(hands, 1)
    # print(hands[winner])
    return score(hands[winner])


def score(hand):
    i = 0
    total = 0
    for card in hand:
        i += 1
        total += i * card
    return total


if __name__ == '__main__':
    testName = "test2020_22a.txt"
    inputName = "input2020_22a.txt"

    print("Part 1: {}".format(playGame(inputName)))
    print("Part 2: {}".format(playRecursiveGame(inputName)))
