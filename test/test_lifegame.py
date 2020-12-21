import unittest
from lifegame import lifegame


class TestSeat(unittest.TestCase):
    def test_init_occupied(self):
        s = lifegame.Seat('#')
        self.assertEqual(True, s.occupied)

    def test_init_unoccupied(self):
        s = lifegame.Seat('L')
        self.assertEqual(False, s.occupied)


class TestLifeGame(unittest.TestCase):
    fInput1a = "input2020_11a.txt"
    fTest1a = "test2020_11a.txt"
    fTest1b = "test2020_11b.txt"
    fTest1c = "test2020_11c.txt"
    fTest1d = "test2020_11d.txt"
    fTest1e = "test2020_11e.txt"
    fTest1f = "test2020_11f.txt"
    fTestSequence1 = ["test2020_11a.txt", "test2020_11b.txt", "test2020_11c.txt", "test2020_11d.txt", "test2020_11e.txt", "test2020_11f.txt"]
    fTestSequence2 = ["test2020_11a.txt", "test2020_11b.txt", "test2020_11c2.txt", "test2020_11d2.txt", "test2020_11e2.txt", "test2020_11f2.txt", "test2020_11g2.txt"]

    def test_init_dimsCorrect_fTest1a(self):
        lg = lifegame.LifeGame(self.fTest1a)
        seatCount = str(lg).count('L') + str(lg).count('#')
        self.assertEqual(10, len(lg.seatingPlan), "Row count.")
        self.assertEqual(10, len(lg.seatingPlan[0]), "Column count.")

    def test_init_matchSeatCount_fTest1a(self):
        lg = lifegame.LifeGame(self.fTest1a)
        seatCount = str(lg).count('L') + str(lg).count('#')
        self.assertEqual(seatCount, len(lg.seatsUnresolved))

    def test_init_neighbourCheck_fTest1a(self):
        lg = lifegame.LifeGame(self.fTest1a)
        seatCount = str(lg).count('L') + str(lg).count('#')
        self.assertEqual(seatCount, len(lg.seatsUnresolved))

    def test_init_SeatCountInvariant_fTestSequence(self):
        lg = lifegame.LifeGame(self.fTest1a)
        seatCount = str(lg).count('L') + str(lg).count('#')
        self.assertEqual(seatCount, len(lg.seatsUnresolved))
        for fileName in self.fTestSequence1:
            lg2 = lifegame.LifeGame(fileName)
            self.assertEqual(seatCount, len(lg.seatsUnresolved), "File: {}\n{}\n\n".format(fileName, lifegame.LifeGame.sideBySide(lg, lg2)))

    def test_eq_fTestSequence(self):
        for fileName in self.fTestSequence1:
            lg1 = lifegame.LifeGame(fileName)
            lg2 = lifegame.LifeGame(fileName)
            self.assertEqual(lg1, lg2, "File: {}\n{}\n\n".format(fileName, lifegame.LifeGame.sideBySide(lg1, lg2)))

    def test_str_equal_fTestSequence(self):
        for fileName in self.fTestSequence1:
            lg1 = str(lifegame.LifeGame(fileName))
            lg2 = str(lifegame.LifeGame(fileName))
            self.assertEqual(lg1, lg2)

    def test_ne_constant_fTestSequence(self):
        lg1 = lifegame.LifeGame(self.fTestSequence1[0])
        for fileName in self.fTestSequence1[1:]:
            lg2 = lifegame.LifeGame(fileName)
            self.assertNotEqual(lg1, lg2, "File: {}\n{}\n\n".format(fileName, lifegame.LifeGame.sideBySide(lg1, lg2)))

    def test_ne_varying_fTestSequence(self):
        lg1 = lifegame.LifeGame(self.fTestSequence1[0])
        for fileName in self.fTestSequence1[1:]:
            lg2 = lifegame.LifeGame(fileName)
            self.assertNotEqual(lg1, lg2, fileName)
            lg1 = lifegame.LifeGame(fileName)

    def test_generations_fTestSequence1(self):
        lg = lifegame.LifeGame(self.fTestSequence1[0])
        gen = 0
        for fileName in self.fTestSequence1:
            lgExpected = lifegame.LifeGame(fileName)
            self.assertEqual(lgExpected.seatingPlan, lg.seatingPlan,
                             "Gen {}: {}\n{}\n\n".format(gen, fileName, lifegame.LifeGame.sideBySide(lgExpected, lg)))
            lg.calculateNextGen()
            lg.iterateGen()
            print(lifegame.LifeGame.sideBySide(lgExpected, lg), end='\n\n')
            gen += 1

    def test_generations_fTestSequence2(self):
        lg = lifegame.LifeGame(self.fTestSequence2[0], immediateAdjacency=False, threshold=5)
        gen = 0
        for fileName in self.fTestSequence2:
            lgExpected = lifegame.LifeGame(fileName)
            self.assertEqual(lgExpected.seatingPlan, lg.seatingPlan,
                             "Gen {}: {}\n{}\n\n".format(gen, fileName, lifegame.LifeGame.sideBySide(lgExpected, lg)))
            print(lifegame.LifeGame.sideBySide(lgExpected, lg), end='\n\n')
            lg.calculateNextGen()
            lg.iterateGen()
            gen += 1

    def test_seatingPlans_equal_fTestSequence(self):
        for fileName in self.fTestSequence1:
            lg1 = lifegame.LifeGame(fileName)
            lg2 = lifegame.LifeGame(fileName)
            self.assertEqual(lg1.seatingPlan, lg2.seatingPlan,
                             "File: {}\n{}\n\n".format(fileName, lifegame.LifeGame.sideBySide(lg1, lg2)))


if __name__ == '__main__':
    unittest.main()
