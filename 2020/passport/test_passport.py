import unittest
import passport

class TestPassport(unittest.TestCase):
    def test_isValidEye_knownBad1(self):
        self.assertEqual(False, passport.isValidEye("wat"))

    def test_isValidEye_knownBad2(self):
        self.assertEqual(False, passport.isValidEye("xry"))

    def test_isValidEye_knownGood(self):
        self.assertTrue(passport.isValidEye("brn"))

    def test_isValidEye_knownGoods(self):
        goods = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        for good in goods:
            self.assertTrue(passport.isValidEye(good), good)

    def test_isValidHair_invalidHex(self):
        self.assertEqual(False, passport.isValidHair("#11111g"))

    def test_isValidHair_knownBad1(self):
        self.assertEqual(False, passport.isValidHair("#123abz"))

    def test_isValidHair_knownBad2(self):
        self.assertEqual(False, passport.isValidHair("123abc"))

    def test_isValidHair_knownGood(self):
        self.assertTrue(passport.isValidHair("#123abc"))

    def test_isValidHair_missingHash(self):
        self.assertEqual(False, passport.isValidHair("111111"))

    def test_isValidHair_ones(self):
        self.assertTrue(passport.isValidHair("#111111"))

    def test_isValidHair_tooLong(self):
        self.assertEqual(False, passport.isValidHair("#1111111"))

    def test_isValidHair_tooShort(self):
        self.assertEqual(False, passport.isValidHair("#11111"))

    def test_isValidHeight_bottomEdge(self):
        self.assertTrue(passport.isValidHeight("150cm"), "Bottom edge inner")
        self.assertEqual(False, passport.isValidHeight("149cm"), "Bottom edge outer")
        self.assertTrue(passport.isValidHeight("59in"), "Bottom edge inner")
        self.assertEqual(False, passport.isValidHeight("58in"), "Bottom edge outer")

    def test_isValidHeight_topEdge(self):
        self.assertTrue(passport.isValidHeight("193cm"), "Top edge inner")
        self.assertEqual(False, passport.isValidHeight("194cm"), "Top edge outer")
        self.assertTrue(passport.isValidHeight("76in"), "Top edge inner")
        self.assertEqual(False, passport.isValidHeight("77in"), "Top edge outer")

    def test_isValidHeight_knownBad_in(self):
        self.assertEqual(False, passport.isValidHeight("190in"))

    def test_isValidHeight_knownGood_cm(self):
        self.assertTrue(passport.isValidHeight("190cm"))

    def test_isValidHeight_knownGood_in(self):
        self.assertTrue(passport.isValidHeight("60in"))

    def test_isValidHeight_noUnits1digit(self):
        self.assertEqual(False, passport.isValidHeight("9"))

    def test_isValidHeight_noUnits2digit(self):
        self.assertEqual(False, passport.isValidHeight("74"))

    def test_isValidHeight_noUnits3digit(self):
        self.assertEqual(False, passport.isValidHeight("190"))

    def test_isValidPID_alpha(self):
        self.assertEqual(False, passport.isValidPID("12a456789"))

    def test_isValidPID_knownBad(self):
        self.assertEqual(False, passport.isValidPID("0123456789"))

    def test_isValidPID_knownGood1(self):
        self.assertTrue(passport.isValidPID("000000001"))

    def test_isValidPID_knownGood2(self):
        self.assertTrue(passport.isValidPID("123456789"))

    def test_isValidPID_tooLong(self):
        self.assertEqual(False, passport.isValidPID("1234567890"))

    def test_isValidPID_tooShort(self):
        self.assertEqual(False, passport.isValidPID("12345678"))

    def test_isYearinRange_bottomEdge1(self):
        self.assertTrue(passport.isYearinRange("1920", 1920, 2002), "Inside edge")
        self.assertEqual(False, passport.isYearinRange("1919", 1920, 2002), "Outside edge")

    def test_isYearinRange_bottomEdge2(self):
        self.assertTrue(passport.isYearinRange("2010", 2010, 2020), "Inside edge")
        self.assertEqual(False, passport.isYearinRange("2009", 2010, 2020), "Outside edge")

    def test_isYearinRange_bottomEdge3(self):
        self.assertTrue(passport.isYearinRange("2020", 2020, 2030), "Inside edge")
        self.assertEqual(False, passport.isYearinRange("2019", 2020, 2030), "Outside edge")

    def test_isYearinRange_tooLongTop(self):
        self.assertEqual(False, passport.isYearinRange("02002", 1920, 2002), "Inside edge")
        self.assertEqual(False, passport.isYearinRange("02003", 1920, 2002), "Outside edge")

    def test_isYearinRange_topEdge1(self):
        self.assertTrue(passport.isYearinRange("2002", 1920, 2002), "Inside edge")
        self.assertEqual(False, passport.isYearinRange("2003", 1920, 2002), "Outside edge")

    def test_isYearinRange_topEdge2(self):
        self.assertTrue(passport.isYearinRange("2020", 2010, 2020), "Inside edge")
        self.assertEqual(False, passport.isYearinRange("2021", 2010, 2020), "Outside edge")

    def test_isYearinRange_topEdge3(self):
        self.assertTrue(passport.isYearinRange("2030", 2020, 2030), "Inside edge")
        self.assertEqual(False, passport.isYearinRange("2031", 2020, 2030), "Outside edge")

    def test_validate_testData_default(self):
        self.assertEqual(2, passport.validCount("test.txt"))

    def test_validate_inputData_default(self):
        self.assertEqual(210, passport.validCount("input.txt"))

    def test_validate_testData_quick(self):
        self.assertEqual(2, passport.validCount("test.txt", passport.validateQuick))

    def test_validate_inputData_quick(self):
        self.assertEqual(210, passport.validCount("input.txt", passport.validateQuick))

    def test_validate_validData_thorough(self):
        self.assertEqual(4, passport.validCount("valid.txt", passport.ValidateThorough))

    def test_validate_mixedData_thorough(self):
        self.assertEqual(4, passport.validCount("mixed.txt", passport.ValidateThorough))

    def test_validate_invalidData_thorough(self):
        self.assertEqual(0, passport.validCount("invalid.txt", passport.ValidateThorough))

    def test_validate_inputData_thorough(self):
        self.assertEqual(131, passport.validCount("input.txt", passport.ValidateThorough))

if __name__ == '__main__':
    unittest.main()
