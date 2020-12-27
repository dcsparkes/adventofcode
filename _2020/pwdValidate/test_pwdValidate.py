import unittest
import pwdValidate


class TestValidate(unittest.TestCase):
    def test_charLimit_a1(self):
        self.assertFalse(pwdValidate.charLimit(2, 5, 'a', "a"), )

    def test_charLimit_a6(self):
        self.assertFalse(pwdValidate.charLimit(2, 5, 'a', "aaaaaa"))

    def test_charLimit_a2_5(self):
        for i in range(2, 6):
            self.assertTrue(pwdValidate.charLimit(2, 5, 'a', "a" * i))

    def test_charLimit_testString1(self):
        line = "1-3 a: abcde"
        self.assertTrue(pwdValidate.checkPwdParams(line))

    def test_charLimit_testString2(self):
        line = "1-3 b: cdefg"
        self.assertFalse(pwdValidate.checkPwdParams(line))

    def test_charLimit_testString3(self):
        line = "2-9 c: ccccccccc"
        self.assertTrue(pwdValidate.checkPwdParams(line))

    def test_parityOddCount_testString1(self):
        line = "1-3 a: abcde"
        self.assertTrue(pwdValidate.checkPwdParams(line, pwdValidate.parityOddCount))

    def test_parityOddCount_testString2(self):
        line = "1-3 b: cdefg"
        self.assertFalse(pwdValidate.checkPwdParams(line, pwdValidate.parityOddCount))

    def test_parityOddCount_testString3(self):
        line = "2-9 c: ccccccccc"
        self.assertFalse(pwdValidate.checkPwdParams(line, pwdValidate.parityOddCount))

    def test_checkFile_default_testFile1(self):
        name = "test.txt"
        self.assertEqual(pwdValidate.checkFile(name), 2)

    def test_checkFile_default_testFile2(self):
        name = "input2.1.txt"
        self.assertEqual(pwdValidate.checkFile(name), 447)

    def test_checkFile_charLimit_testFile1(self):
        name = "test.txt"
        self.assertEqual(pwdValidate.checkFile(name, pwdValidate.charLimit), 2)

    def test_checkFile_charLimit_testFile2(self):
        name = "input2.1.txt"
        self.assertEqual(pwdValidate.checkFile(name, pwdValidate.charLimit), 447)

    def test_checkFile_parityOddCount_testFile1(self):
        name = "test.txt"
        self.assertEqual(pwdValidate.checkFile(name, pwdValidate.parityOddCount), 1)

    def test_checkFile_parityOddCount_testFile2(self):
        name = "input2.1.txt"
        self.assertEqual(pwdValidate.checkFile(name, pwdValidate.parityOddCount), 249)

if __name__ == '__main__':
    unittest.main()

