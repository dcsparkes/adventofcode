"""
https://adventofcode.com/2015/day/22
"""


class Wizard:
    cheapestSolution = None
    cheapestSolutionCost = None

    spells = {  # name: (cost, duration, damage, heal, acBonus, manaRecharge)
        "Magic Missile": (53, 1, 4, 0, 0, 0),
        "Drain": (73, 1, 2, 2, 0, 0),
        "Shield": (113, 6, 0, 0, 7, 0),
        "Poison": (173, 6, 3, 0, 0, 0),
        "Recharge": (229, 5, 0, 0, 0, 101),
    }

    def __init__(self, opponentHP, opponentDamage):
        self.opponentHP = opponentHP
        self.opponentDamage = opponentDamage
        self.hp = 50
        self.mana = 500
        self.baseAC = 0

    def _opponentRound(self, hp, mana, totalspent, opponentHP, spellsCast, activeSpells):
        if self.cheapestSolutionCost and totalspent > self.cheapestSolutionCost:
            return False
        # Opponent Round: Evaluate active spell effects
        dam, heal, acBonus, manaBoost = self._evaluateSpellEffects(activeSpells)
        opponentHP -= dam
        if opponentHP <= 0 and (not self.cheapestSolutionCost or totalspent < self.cheapestSolutionCost):
            self.cheapestSolutionCost = totalspent
            self.cheapestSolution = spellsCast
        hp += heal
        ac = self.baseAC + acBonus
        mana += manaBoost

        # Opponent Round: deal damage
        damage = max(1, self.opponentDamage - ac)
        hp -= damage
        if hp <= 0:  # Death
            return False

        return self._wizardRound(hp, mana, totalspent, opponentHP, spellsCast, activeSpells)

    def _wizardRound(self, hp, mana, totalspent, opponentHP, spellsCast, activeSpells):
        # Wizard Round: Evaluate active spell effects
        dam, heal, acBonus, manaBoost = self._evaluateSpellEffects(activeSpells)
        opponentHP -= dam
        if opponentHP <= 0 and (not self.cheapestSolutionCost or totalspent < self.cheapestSolutionCost):
            self.cheapestSolutionCost = totalspent
            self.cheapestSolution = spellsCast
        hp += heal
        mana += manaBoost

        retVal = False
        for spell, values in self.spells.items():
            cost = values[0]
            if cost < mana:  # If spell can be cast branch the timeline into casting it
                activeSpellCopy = dict(activeSpells)
                activeSpellCopy[spell] = values[1]
                spellsCastCopy = spellsCast[:]
                spellsCastCopy.append(spell)
                retVal |= self._opponentRound(hp, mana - cost, totalspent + cost, opponentHP, spellsCastCopy,
                                              activeSpellCopy)
        return retVal

    def _evaluateSpellEffects(self, activeSpells):
        effects = [(0, 0, 0, 0)]
        toBeDeleted = []
        for spell in activeSpells:
            effects.append(self.spells[spell][2:])
            activeSpells[spell] -= 1
            if not activeSpells[spell]:
                toBeDeleted.append(spell)
        for spell in toBeDeleted:
            del activeSpells[spell]
        return [sum(l) for l in zip(*effects)]

    def startCombats(self):
        self._wizardRound(self.hp, self.mana, 0, self.opponentHP, [], {})
        return self.cheapestSolutionCost, self.cheapestSolution


if __name__ == '__main__':
    w = Wizard(51, 9)
    print("Part 1: {}".format(w.startCombats()))
    # print("Part 2: {}".format(w))
