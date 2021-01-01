"""
https://adventofcode.com/2020/day/24
"""
import unittest
from lobbylayout import lobbylayout


class TestLifeGame2DHex(unittest.TestCase):
    fInput = "input2020_24a.txt"
    fTest1a = "test2020_24a.txt"

    def test_play_fTest1a_10(self):
        ts = lobbylayout.TileSet(self.fTest1a)
        genCounts = ts.playGame(10)
        self.assertEqual([10, 15, 12, 25, 14, 23, 28, 41, 37, 49, 37], genCounts)

    def test_play_fInput_100sliced(self):
        expectedCounts = [282, 337, 553, 745, 1086, 1389, 1776, 2071, 2482, 3035, 3445]
        ts = lobbylayout.TileSet(self.fInput)
        genCounts = ts.playGame(100)
        self.assertEqual(expectedCounts, genCounts[0::10])

    def test_play_fTest1a_100sliced(self):
        expectedCounts = [10, 37, 132, 259, 406, 566, 788, 1106, 1373, 1844, 2208]
        ts = lobbylayout.TileSet(self.fTest1a)
        genCounts = ts.playGame(100)
        self.assertEqual(expectedCounts, genCounts[0::10])

    def test_play_fTest1a_100(self):
        ts = lobbylayout.TileSet(self.fTest1a)
        genCounts = ts.playGame(100)
        self.assertEqual([10, 15, 12, 25, 14, 23, 28, 41, 37, 49, 37], genCounts[:11])
        self.assertEqual(132, genCounts[20])
        self.assertEqual(259, genCounts[30])
        self.assertEqual(406, genCounts[40])
        self.assertEqual(566, genCounts[50])
        self.assertEqual(788, genCounts[60])
        self.assertEqual(1106, genCounts[70])
        self.assertEqual(1373, genCounts[80])
        self.assertEqual(1844, genCounts[90])
        self.assertEqual(2208, genCounts[-1])


class TestCube2DHex(unittest.TestCase):
    def test_neighbours_refCoordsMatchExpected(self):
        cube = lobbylayout.Cube2DHex((0, 0))
        expectedCoords = [(-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0)]
        for coord in cube.neighbours():
            self.assertTrue(coord in expectedCoords)

    def test_neighbours_refCoordCount(self):
        cube = lobbylayout.Cube2DHex((9, -8))
        coords = list(cube.neighbours())
        expectedCoords = [(-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0)]
        self.assertEqual(len(coords), len(expectedCoords))

    def test_neighbours_refCoordsExactMatch(self):
        cube = lobbylayout.Cube2DHex((0, 0))
        coords = list(cube.neighbours())
        expectedCoords = [(-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0)]
        self.assertEqual(coords, expectedCoords)


class TestLobbyLayout(unittest.TestCase):
    fInput = "input2020_24a.txt"
    fTest1a = "test2020_24a.txt"

    def test_readMyFlips_fInput(self):
        ts = lobbylayout.TileSet()
        ts.readMyFlips(self.fInput)
        self.assertEqual(282, ts.flippedCount())

    def test_readMyFlips_fTest1a(self):
        ts = lobbylayout.TileSet()
        ts.readMyFlips(self.fTest1a)
        self.assertEqual(10, ts.flippedCount())

    def test_flip_single(self):
        ts = lobbylayout.TileSet()
        ts.flip("esenee")
        self.assertEqual(1, ts.flippedCount())

    def test_flip_reference(self):
        ts = lobbylayout.TileSet()
        ts.flip("nwwswee")
        self.assertEqual(1, ts.flippedCount())
        self.assertTrue(ts.referenceCoords in ts.flippedTiles)


if __name__ == '__main__':
    unittest.main()
