import unittest
from tokentree import tokentree


class TestRuleTree(unittest.TestCase):
    fInput = "input2020_19a.txt"
    fTest = "test2020_19a.txt"

    def test_RuleTree_nonBranchingNonTerminals(self):
        rt = tokentree.RuleTree("56: 105 39")
        expected = "RuleTree(id=56, nonTerminals=[('105', '39')])"
        self.assertEqual(expected, str(rt))

    def test_RuleTree_terminal(self):
        rt = tokentree.RuleTree("105: \"b\"")
        expected = "RuleTree(id=105, terminal=b)"
        self.assertEqual(expected, str(rt))

    def test_RuleTree_branchingNonTerminals(self):
        rt = tokentree.RuleTree("120: 105 131 | 23 44")
        expected = "RuleTree(id=120, nonTerminals=[('105', '131'), ('23', '44')])"
        self.assertEqual(expected, str(rt))



class TestPlanter(unittest.TestCase):
    fInput = "input2020_19a.txt"
    fTest = "test2020_19a.txt"

    def test_Planter_(self):
        p = tokentree.Planter(self.fTest)



if __name__ == '__main__':
    unittest.main()
