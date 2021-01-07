import adventCoinMiner
import hashlib
import unittest

class TestAdventCoinMiner(unittest.TestCase):
    def setUp(self):
        self.acm = adventCoinMiner.AdventCoinMiner()

    def test_AdventCoinMiner_abcdef(self):
        self.assertEqual(609043, self.acm.solve("abcdef"))

    def test_AdventCoinMiner_pqrstuv(self):
        self.assertEqual(1048970, self.acm.solve("pqrstuv"))

    def test_AdventCoinMiner_ckczppom_fiveZeroes(self):
        self.assertEqual(117946, self.acm.solve("ckczppom"))

    def test_AdventCoinMiner_ckczppom_sixZeroes(self):
        self.assertEqual(3938038, self.acm.solve("ckczppom", "000000"))

    def test_hashlib_abcdef609043(self):
        hash = hashlib.md5("abcdef609043".encode('utf-8')).hexdigest()
        check = "000001dbbfa"
        self.assertEqual(check, hash[:len(check)])

    def test_hashlib_abcdef(self):
        hash = hashlib.md5("pqrstuv1048970".encode('utf-8')).hexdigest()
        check = "000006136ef"
        self.assertEqual(check, hash[:len(check)])

if __name__ == '__main__':
    unittest.main()
