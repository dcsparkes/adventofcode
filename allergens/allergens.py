"""
https://adventofcode.com/2020/day/21
"""
from base import base


class Allergens:
    def __init__(self):
        self.ingredientCounts = {}
        self.allergenCandidates = {}
        self.ingredientsResolved = {}
        self.part1 = None
        self.part2 = None

    def _processLine(self, line):
        ings, alls = line.strip(' \n\t()').split(" (contains ")
        ingredients = ings.split(' ')
        allergens = alls.split(', ')
        return ingredients, allergens

    def readFile(self, fileName):
        for line in base.getInputLines(fileName):
            ingredients, allergens = self._processLine(line)
            # print("ingredients: {}, allergens: {}".format(ingredients, allergens))
            for allergen in allergens:
                unAllocatedIngredients = [i for i in ingredients if i not in self.ingredientsResolved]
                if allergen not in self.allergenCandidates:
                    self.allergenCandidates[allergen] = set(unAllocatedIngredients)
                else:
                    self.allergenCandidates[allergen] &= set(unAllocatedIngredients)
                if len(self.allergenCandidates[allergen]) == 1:
                    candidate = self.allergenCandidates[allergen].pop()
                    self.ingredientsResolved[candidate] = allergen
            for ingredient in ingredients:
                if ingredient in self.ingredientCounts:
                    self.ingredientCounts[ingredient] += 1
                else:
                    self.ingredientCounts[ingredient] = 1

        resolved = True
        while resolved:
            resolved = False
            toBeDeleted = []
            for allergen, candidates in self.allergenCandidates.items():
                if len(candidates) > 0:
                    candidates -= set([k for k in self.ingredientsResolved.keys()])

                if len(candidates) == 1:
                    candidate = self.allergenCandidates[allergen].pop()
                    self.ingredientsResolved[candidate] = allergen
                    resolved = True
                if not len(candidates):
                    toBeDeleted.append(allergen)
            for candidate in toBeDeleted:
                del self.allergenCandidates[candidate]

        self.part1 = sum([val for k, val in self.ingredientCounts.items() if k not in self.ingredientsResolved])
        sortedByValue = sorted(self.ingredientsResolved.items(), key=lambda kv: kv[1])
        self.part2 = ','.join([k for k, v in sortedByValue])

if __name__ == '__main__':
    a = Allergens()
    a.readFile("input2020_21a.txt")
    print("Part1: {}".format(a.part1))
    print("Part2: {}".format(a.part2))




