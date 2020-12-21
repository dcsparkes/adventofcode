import roomcheck
import unittest


class TestRoom(unittest.TestCase):
    alphas = "abcdefghijklmnopqrstuvwxyz"
    knownBad1 = "totally-real-room-200[decoy]"
    knownGood1 = "aaaaa-bbb-z-y-x-123[abxyz]"
    knownGood2 = "a-b-c-d-e-f-g-h-987[abcde]"
    knownGood3 = "not-a-real-room-404[oarel]"

    def test_add_ToInt_default(self):
        r1 = roomcheck.Room()
        for i in range(7):
            self.assertEqual(i, r1 + i, i)

    def test_radd_IntTo_default(self):
        r1 = roomcheck.Room()
        for i in range(7):
            self.assertEqual(i, i + r1, i)

    def test_add_ToInt_knownGood3(self):
        r1 = roomcheck.Room(self.knownGood3)
        for i in range(7):
            self.assertEqual(404 + i, r1 + i, i)

    def test_radd_IntTo_knownGood3(self):
        r1 = roomcheck.Room(self.knownGood3)
        for i in range(7):
            self.assertEqual(404 + i, i + r1, i)

    def test_bool_default(self):
        r1 = roomcheck.Room()
        self.assertFalse(r1)

    def test_bool_knownBad(self):
        r1 = roomcheck.Room(self.knownBad1)
        self.assertFalse(r1)

    def test_bool_knownGood1(self):
        r1 = roomcheck.Room(self.knownGood1)
        self.assertTrue(r1)

    def test_bool_knownGood2(self):
        r1 = roomcheck.Room(self.knownGood2)
        self.assertTrue(r1)

    def test_bool_knownGood3(self):
        r1 = roomcheck.Room(self.knownGood3)
        self.assertTrue(r1)

    def test_decodeName_complementaryRotation(self):
        text = "nopqrstuvwxy-zabcdefghijklm"
        n = 26
        f = roomcheck.Room._decodeName
        for base in range(19):
            for i in range(n):
                out = base * n + i
                back = 1014 - i
                msg = "out: {}, back: {}".format(out, back)
                self.assertEqual(text, f(f(text, out), back), msg)

    def test_decodeName_known4(self):
        self.assertEqual("very encrypted name", roomcheck.Room._decodeName("qzmt-zixmtkozy-ivhz", 343))

    def test_makeLookup_rot1(self):
        lookup = roomcheck.Room._makeLookup(1)
        self.assertEqual('b', lookup['a'])

    def test_makeLookup_rotNs(self):
        for i in range(26):
            lookup = roomcheck.Room._makeLookup(i)
            self.assertEqual(self.alphas[i], lookup['a'], i)

    def test_decode_known4(self):
        r1 = roomcheck.Room(nameEncoded="qzmt-zixmtkozy-ivhz", sectorID=343, isValid=True)
        self.assertEqual("very encrypted name", r1.name)

    def test_addTwoRooms_known(self):
        r1 = roomcheck.Room(self.knownGood1)
        r2 = roomcheck.Room(self.knownGood2)
        self.assertEqual(123 + 987, r1 + r2)

    def test_addTwoRooms_default(self):
        r1 = roomcheck.Room()
        r2 = roomcheck.Room()
        self.assertEqual(0, r1 + r2)

    def test_sumRooms_default(self):
        r1 = (roomcheck.Room(self.knownGood1), roomcheck.Room(self.knownGood2), roomcheck.Room(self.knownGood3))
        self.assertEqual(123 + 404 + 987, sum(r1))


class TestRoomCheck(unittest.TestCase):
    fTestA = "test2016_04a.txt"
    fInput = "input2016_04a.txt"

    def test_init(self):
        rc = roomcheck.RoomCheck()
        # ts.readFile("input2016_03a.txt")
        self.assertEqual(0, rc.countValid())

    def test_sanityCheck_valid_le_total_fTestA(self):
        rc = roomcheck.RoomCheck()
        rc.readFile(self.fTestA)
        self.assertTrue(rc.countValid() <= len(rc.candidates))

    def test_sanityCheck_valid_lt_total_fTestA(self):
        rc = roomcheck.RoomCheck()
        rc.readFile(self.fTestA)
        self.assertTrue(rc.countValid() <= len(rc.candidates))

    def test_printValid_fInput(self):
        rc = roomcheck.RoomCheck()
        rc.readFile(self.fInput)
        rc.printValid()
        # self.assertEqual(409147, rc.sum())

    def test_sum_default(self):
        rc = roomcheck.RoomCheck()
        self.assertEqual(0, rc.sum())

    def test_sum_fInput(self):
        rc = roomcheck.RoomCheck()
        rc.readFile(self.fInput)
        self.assertEqual(409147, rc.sum())

    def test_sum_fTestA(self):
        rc = roomcheck.RoomCheck()
        rc.readFile(self.fTestA)
        self.assertEqual(1514, rc.sum())

if __name__ == '__main__':
    unittest.main()
