"""
https://adventofcode.com/2020/day/19

"""
import unittest
from tokentree import tokentree


class TestTokenTrie(unittest.TestCase):
    alpha6 = "abcdef"

    def test_iadd_branchingTree_self(self):
        ts = ["abc", "cba", "cde"]
        tree = tokentree.TokenTrie()
        for t in ts:
            tree.insert(t)
        tree += tree

        for t1 in ts:
            self.assertFalse(t in tree, t)
            for t2 in ts:
                token = ''.join([t1, t2])
                self.assertTrue(token in tree, token)

    def test_insert_branchingTree_self(self):
        ts = ["abc", "cba", "cde"]
        tree = tokentree.TokenTrie()
        for t in ts:
            tree.insert(t)

        for t in ts:
            self.assertTrue(t in tree, t)

    def test_iadd_branchingTreeAppended(self):
        t1 = "abc"
        t2 = "cba"
        t3 = "cde"
        tree1 = tokentree.TokenTrie(t1)
        tree2 = tokentree.TokenTrie(t2)
        tree2 |= tokentree.TokenTrie(t3)  # Union merges trees
        tree1 += tree2  # Append concatenates token sequences
        token1 = t1 + t2
        token2 = t1 + t3
        self.assertTrue(token1 in tree1, "Testing <{}>".format(token1))
        self.assertTrue(token2 in tree1, "Testing <{}>".format(token2))
        self.assertFalse(t1 in tree1, "Testing t1<{}>".format(t1))  # t1  should no longer be a valid token

    def test_iadd_branchingTreeAppendee(self):
        t1 = "abc"
        t2 = "cba"
        t3 = "cde"
        tree1 = tokentree.TokenTrie(t1)
        tree2 = tokentree.TokenTrie(t2)
        tree2 |= tokentree.TokenTrie(t3)  # Union merges trees
        tree2 += tree1  # Append concatenates token sequences
        token1 = t2 + t1
        token2 = t3 + t1
        self.assertTrue(token1 in tree2, "Testing <{}>".format(token1))
        self.assertTrue(token2 in tree2, "Testing <{}>".format(token2))
        self.assertFalse(t1 in tree2, "Testing t1<{}>".format(t1))  # t1 should not be a valid token
        self.assertFalse(t2 in tree2, "Testing t2<{}>".format(t2))  # t2 should no longer be a valid token
        self.assertFalse(t3 in tree2, "Testing t3<{}>".format(t3))  # t3 should no longer be a valid token

    def test_ior_empty(self):
        t2 = "cba"
        t3 = "cde"
        tree1 = tokentree.TokenTrie()
        tree1 |= tokentree.TokenTrie(t2)
        tree1 |= tokentree.TokenTrie(t3)
        self.assertTrue(t2 in tree1, "Testing t2: <{}>".format(t2))
        self.assertTrue(t3 in tree1, "Testing t3: <{}>".format(t3))

    def test_ior_branchingTree(self):
        t2 = "cba"
        t3 = "cde"
        tree2 = tokentree.TokenTrie(t2)
        tree2 |= tokentree.TokenTrie(t3)
        self.assertTrue(t2 in tree2, "Testing t2: <{}>".format(t2))
        self.assertTrue(t3 in tree2, "Testing t3: <{}>".format(t3))

    def test_ior_substringTree(self):
        substrLen = 3
        tree = tokentree.TokenTrie(self.alpha6)
        tree2 = tokentree.TokenTrie(self.alpha6[:substrLen])
        tree |= tree2
        self.assertTrue(self.alpha6 in tree)
        self.assertTrue(self.alpha6[:substrLen] in tree)
        self.assertFalse(self.alpha6[:substrLen + 1] in tree)
        self.assertFalse(self.alpha6[:substrLen - 1] in tree)

    def test_ior_substringTreeDoesNotChangeOther(self):
        substrLen = 3
        tree = tokentree.TokenTrie(self.alpha6)
        tree2 = tokentree.TokenTrie(self.alpha6[:substrLen])
        tree |= tree2
        self.assertFalse(self.alpha6 in tree2)
        self.assertTrue(self.alpha6[:substrLen] in tree2)
        self.assertFalse(self.alpha6[:substrLen + 1] in tree2)
        self.assertFalse(self.alpha6[:substrLen - 1] in tree2)

    def test_ior_substring(self):
        substrLen = 4
        tree = tokentree.TokenTrie(self.alpha6)
        tree |= self.alpha6[:substrLen]
        self.assertTrue(self.alpha6 in tree)
        self.assertTrue(self.alpha6[:substrLen] in tree)
        self.assertFalse(self.alpha6[:substrLen + 1] in tree)
        self.assertFalse(self.alpha6[:substrLen - 1] in tree)

    def test_add_substring(self):
        substrLen = 4
        tree = tokentree.TokenTrie(self.alpha6)
        tree.insert(self.alpha6[:substrLen])
        self.assertTrue(self.alpha6 in tree)
        self.assertTrue(self.alpha6[:substrLen] in tree)

    def test_add_self(self):
        tree = tokentree.TokenTrie(self.alpha6)
        tree += tree
        self.assertFalse(self.alpha6 in tree)
        self.assertTrue(self.alpha6 * 2 in tree)

    def test_len_alpha6(self):
        tree = tokentree.TokenTrie(self.alpha6)
        self.assertEqual(1 + len(self.alpha6), len(tree))

    def test_contains_alpha6(self):
        tree = tokentree.TokenTrie(self.alpha6)
        self.assertTrue(self.alpha6 in tree)

    def test_contains_alpha6_tooLong(self):
        tree = tokentree.TokenTrie(self.alpha6)
        self.assertFalse(self.alpha6 + "a" in tree)

    def test_contains_alpha6_tooShort(self):
        tree = tokentree.TokenTrie(self.alpha6)
        self.assertFalse(self.alpha6[:-1] in tree)

    def test_contains_emptyToken(self):
        tree = tokentree.TokenTrie("")
        self.assertTrue("" in tree)

    def test_len_emptyToken(self):
        tree = tokentree.TokenTrie("")
        self.assertEqual(1, len(tree))

    def test_len_emptyTree(self):
        tree = tokentree.TokenTrie()
        self.assertEqual(1, len(tree))


class TestRuleTree(unittest.TestCase):
    fInput = "input2020_19a.txt"
    fTest = "test2020_19a.txt"

    def test_RuleTree_nonBranchingNonTerminals(self):
        rt = tokentree.RuleSet("56: 105 39")
        expected = "RuleSet(id=56, nonTerminals=[('105', '39')])"
        # self.assertEqual(expected, str(rt))
        self.assertEqual("56", rt.id)
        self.assertEqual([('105', '39')], rt.nonTerminals)
        self.assertEqual(set(['105', '39']), rt.waiting)

    def test_RuleTree_terminal(self):
        rt = tokentree.RuleSet("105: \"b\"")
        expected = "RuleSet(id=105)"
        self.assertEqual(expected, str(rt)[:len(expected)])

    def test_RuleTree_branchingNonTerminals(self):
        rt = tokentree.RuleSet("120: 105 131 | 23 44")
        # expected = "RuleSet(id=120, nonTerminals=[('105', '131'), ('23', '44')])"
        self.assertEqual("120", rt.id)
        self.assertEqual([('105', '131'), ('23', '44')], rt.nonTerminals)
        self.assertEqual(set(['105', '131', '23', '44']), rt.waiting)

    def test_RuleTree_branchingNonTerminals_duplicateRuleIDs(self):
        rt = tokentree.RuleSet("120: 105 131 | 23 23")
        # expected = "RuleSet(id=120, nonTerminals=[('105', '131'), ('23', '44')])"
        self.assertEqual("120", rt.id)
        self.assertEqual([('105', '131'), ('23', '23')], rt.nonTerminals)
        self.assertEqual(set(['105', '131', '23']), rt.waiting)


class TestPlanter(unittest.TestCase):
    fInputA = "input2020_19a.txt"
    fInputB = "input2020_19b.txt"  # Hack to include self-referential rules. Could try to figure out how to loop trees?
    fTestA = "test2020_19a.txt"
    fTestB = "test2020_19b.txt"
    fTestC = "test2020_19c.txt"
    fTestD = "test2020_19d.txt"
    fTestE = "test2020_19e.txt"

    # def test_Planter_fInputA(self):
    #     p = tokentree.Planter(self.fInputA)
    #     self.assertEqual(144, len(p.tokensValid))

    def test_Planter_fTestA(self):
        p = tokentree.Planter(self.fTestA)
        self.assertEqual(2, len(p.tokensValid))

    def test_Planter_fTestA_root2_knownBad(self):
        p = tokentree.Planter(self.fTestA, rootRule="2")
        self.assertTrue("aa" in p.tokenValidator, "aa")
        self.assertTrue("bb" in p.tokenValidator, "bb")

    def test_Planter_fTestA_root2_knownGood(self):
        p = tokentree.Planter(self.fTestA, rootRule="2")
        self.assertFalse("ab" in p.tokenValidator, "ab")
        self.assertFalse("ba" in p.tokenValidator, "ba")

    def test_Planter_fTestA_root3_knownGood(self):
        p = tokentree.Planter(self.fTestA, rootRule="3")
        self.assertFalse("aa" in p.tokenValidator, "aa")
        self.assertFalse("bb" in p.tokenValidator, "bb")

    def test_Planter_fTestA_root3_knownBad(self):
        p = tokentree.Planter(self.fTestA, rootRule="3")
        self.assertTrue("ab" in p.tokenValidator, "ab")
        self.assertTrue("ba" in p.tokenValidator, "ba")

    def test_Planter_fTestB(self):
        p = tokentree.Planter(self.fTestB)
        self.assertEqual(2, len(p.tokensValid))

    def test_Planter_fTestC(self):
        p = tokentree.Planter(self.fTestC)
        self.assertEqual(2, len(p.tokensValid))

    def test_Planter_fTestD(self):
        p = tokentree.Planter(self.fTestD)
        self.assertEqual(3, len(p.tokensValid))

    # Very long running test
    # def test_Planter_fTestE(self):
    #     p = tokentree.Planter(self.fTestE)
    #     self.assertEqual(12, len(p.tokensValid))

    def test_Planter_knownBadStrings(self):
        p = tokentree.Planter(self.fTestA)
        for s in ["bababa", "aaabbb", "aaaabbb"]:
            self.assertFalse(s in p.tokenValidator, s)

    def test_Planter_knownGoodStrings(self):
        p = tokentree.Planter(self.fTestA)
        for s in ["ababbb", "abbbab"]:
            self.assertTrue(s in p.tokenValidator, s)




if __name__ == '__main__':
    unittest.main()
