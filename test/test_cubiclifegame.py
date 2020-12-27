import unittest
from lifegame import cubiclifegame


class TestLifeGame(unittest.TestCase):
    fInput1a = "input2020_17a.txt"
    fTest1a = "test2020_17a.txt"

    def test_init_matchSeatCount_3D_fTest1a(self):
        lg = cubiclifegame.LifeGame.threeD(self.fTest1a)
        self.assertEqual(5, lg.getActiveCubeCount())

    def test_init_matchSeatCount_3D_fInput1a(self):
        lg = cubiclifegame.LifeGame.threeD(self.fInput1a)
        self.assertEqual(37, lg.getActiveCubeCount())

    def test_init_matchSeatCount_3D_none(self):
        lg = cubiclifegame.LifeGame.threeD(None)
        self.assertEqual(0, lg.getActiveCubeCount())

    def test_init_matchSeatCount_4D_fTest1a(self):
        lg = cubiclifegame.LifeGame.fourD(self.fTest1a)
        self.assertEqual(5, lg.getActiveCubeCount())

    def test_init_matchSeatCount_4D_fInput1a(self):
        lg = cubiclifegame.LifeGame.fourD(self.fInput1a)
        self.assertEqual(37, lg.getActiveCubeCount())

    def test_playGame_matchSeatCount_3D_fTest1a(self):
        lg = cubiclifegame.LifeGame.threeD(self.fTest1a)
        lg.playGame(6)
        self.assertEqual(112, lg.getActiveCubeCount())

    def test_playGame_matchSeatCount_3D_fInput1a(self):
        lg = cubiclifegame.LifeGame.threeD(self.fInput1a)
        lg.playGame(6)
        self.assertEqual(424, lg.getActiveCubeCount())

    def test_playGame_matchSeatCount_4D_fTest1a(self):
        lg = cubiclifegame.LifeGame.fourD(self.fTest1a)
        lg.playGame(6)
        self.assertEqual(848, lg.getActiveCubeCount())

    def test_playGame_matchSeatCount_4D_fInput1a(self):
        lg = cubiclifegame.LifeGame.fourD(self.fInput1a)
        lg.playGame(6)
        self.assertEqual(2460, lg.getActiveCubeCount())


if __name__ == '__main__':
    unittest.main()
