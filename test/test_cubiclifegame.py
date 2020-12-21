import unittest
from lifegame import cubiclifegame


class TestCube(unittest.TestCase):
    pass
    # def test_init_occupied(self):
    #     s = lifegame.Seat('#')
    #     self.assertEqual(True, s.occupied)
    #
    # def test_init_unoccupied(self):
    #     s = lifegame.Seat('L')
    #     self.assertEqual(False, s.occupied)


class TestLifeGame(unittest.TestCase):
    fInput1a = "input2020_17a.txt"
    fTest1a = "test2020_17a.txt"

    def test_init_matchSeatCount_3D_fTest1a(self):
        lg = cubiclifegame.LifeGame3D(self.fTest1a)
        self.assertEqual(112, lg.getActiveCubeCount())

    def test_init_matchSeatCount_3D_fInput1a(self):
        lg = cubiclifegame.LifeGame3D(self.fInput1a)
        self.assertEqual(424, lg.getActiveCubeCount())

    def test_init_matchSeatCount_4D_fTest1a(self):
        lg = cubiclifegame.LifeGame4D(self.fTest1a)
        self.assertEqual(848, lg.getActiveCubeCount())

    def test_init_matchSeatCount_4D_fInput1a(self):
        lg = cubiclifegame.LifeGame4D(self.fInput1a)
        self.assertEqual(2460, lg.getActiveCubeCount())



if __name__ == '__main__':
    unittest.main()
