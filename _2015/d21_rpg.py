"""
https://adventofcode.com/2015/day/21
"""


class Outfitter:
    weapons = {8: ("Dagger", 4, 0), 10: ("Shortsword", 5, 0), 25: ("Warhammer", 6, 0), 40: ("Longsword", 7, 0),
               74: ("Greataxe", 8, 0)}
    armours = {0: ("Unarmoured", 0, 0), 13: ("Leather", 0, 1), 31: ("Chainmail", 0, 2), 53: ("Splintmail", 0, 3),
               75: ("Bandedmail", 0, 4), 102: ("Platemail", 0, 5)}
    rings = {0: ("None", 0, 0), 25: ("Damage +1", 1, 0), 50: ("Damage +2", 2, 0), 100: ("Damage +3", 3, 0),
             20: ("Defense +1", 0, 1), 40: ("Defense +2", 0, 2), 80: ("Defense +3", 0, 3)}
    permutations = {}

    def __init__(self):
        if not self.permutations:
            self.permutations = sorted(
                [(a + b + c + d, a, b, c, d)
                 for a in self.weapons.keys() for b in self.armours.keys()
                 for c in self.rings.keys() for d in self.rings.keys() if not c or c < d])

    def outfitsAsc(self):
        for p in self.permutations:
            yield p

    def outfitsDesc(self):
        for p in reversed(self.permutations):
            yield p

    def stats(self, outfit):
        cost, weap, armo, ring1, ring2 = outfit
        pivoted = list(zip(*[self.weapons[weap], self.armours[armo], self.rings[ring1], self.rings[ring2]]))
        loadout = ', '.join(pivoted[0])
        dam = sum(pivoted[1])
        ac = sum(pivoted[2])
        return cost, loadout, dam, ac


class Arena:
    outfitter = Outfitter()

    def __init__(self, protHP, oppHP, oppDam, oppArmour):
        self.protHP = protHP
        self.oppHP = oppHP
        self.oppDam = oppDam
        self.oppArmour = oppArmour

    def fightWon(self, protagonistDamage, protagonistAC):
        netProtagonistDamage = max(protagonistDamage - self.oppArmour, 1)
        netOpponentDamage = max(self.oppDam - protagonistAC, 1)
        roundsToKill = -(-self.oppHP // netProtagonistDamage)
        roundsToDie = -(-self.protHP // netOpponentDamage)
        return roundsToKill <= roundsToDie

    def findCheapestWinner(self):
        for outfit in self.outfitter.outfitsAsc():
            cost, loadout, dam, ac = self.outfitter.stats(outfit)
            if self.fightWon(dam, ac):
                return "'{}' wins at a cost of {}".format(loadout, cost)

    def findDearestLoser(self):
        for outfit in self.outfitter.outfitsDesc():
            cost, loadout, dam, ac = self.outfitter.stats(outfit)
            if not self.fightWon(dam, ac):
                return "'{}' loses at a cost of {}".format(loadout, cost)


if __name__ == '__main__':
    a = Arena(100, 100, 8, 2)
    print("Part 1: {}".format(a.findCheapestWinner()))
    print("Part 2: {}".format(a.findDearestLoser()))
