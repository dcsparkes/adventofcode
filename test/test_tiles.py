import unittest
from tiles import tiles


class TestTiles(unittest.TestCase):
    tile1 = ["Tile 1", "..#", ".##", "..#"]
    t1Sides = [(1, 4), (7, 7), (1, 4), (0, 0)]

    tile2 = ["Tile 2", "...#", "..##", "###.", ".###"]
    t2Sides = [(1, 8), (11, 13), (7, 14), (2, 4)]

    def test_init_sideIDcalculation_3x3(self):
        t = tiles.Tile(self.tile1)
        self.assertEqual(self.t1Sides, t.sideIDs)

    def test_init_sideIDcalculation_4x4(self):
        t = tiles.Tile(self.tile2)
        self.assertEqual(self.t2Sides, t.sideIDs)

    def test_rotate90_corners_3x3(self):
        t = tiles.Tile(self.tile1)
        orig = str(t).split('\n')
        t.rotate90()
        newT = str(t).split('\n')
        self.assertEqual(orig[0][0], newT[0][-1], "Top left -> top right")
        self.assertEqual(orig[0][1], newT[1][-1], "Top middle -> middle right")
        self.assertEqual(orig[0][-1], newT[-1][-1], "Top right -> bottom right")
        self.assertEqual(orig[1][0], newT[0][1], "Middle left -> top middle")
        self.assertEqual(orig[1][1], newT[1][1], "Centre -> centre")
        self.assertEqual(orig[1][-1], newT[-1][1], "Middle right -> bottom middle")
        self.assertEqual(orig[-1][0], newT[0][0], "Bottom left -> top left")
        self.assertEqual(orig[-1][1], newT[1][0], "Bottom middle -> middle left")
        self.assertEqual(orig[-1][-1], newT[-1][0], "Bottom right -> bottom left")

    def test_rotate90_corners_4x4(self):
        t = tiles.Tile(self.tile2)
        orig = str(t).split('\n')
        t.rotate90()
        newT = str(t).split('\n')
        self.assertEqual(orig[0][0], newT[0][-1], "Top left -> top right")
        self.assertEqual(orig[0][1], newT[1][-1], "Top left-middle -> above-middle right")
        self.assertEqual(orig[0][-1], newT[-1][-1], "Top right -> bottom right")
        self.assertEqual(orig[1][0], newT[0][-2], "Above-middle left -> top right-middle")
        self.assertEqual(orig[1][-1], newT[-1][-2], "Below-middle right -> bottom left-middle")
        self.assertEqual(orig[-1][0], newT[0][0], "Bottom left -> top left")
        self.assertEqual(orig[-1][1], newT[1][0], "Bottom middle -> middle left")
        self.assertEqual(orig[-1][-1], newT[-1][0], "Bottom right -> bottom left")

    def test_rotate90_full_rotation_360degrees(self):
        t = tiles.Tile(self.tile1)
        orig = str(t)
        for i in range(4):
            t.rotate90()
        self.assertEqual(orig, str(t))

    def test_rotate180_full_rotation_360degrees(self):
        t = tiles.Tile(self.tile1)
        orig = str(t)
        for i in range(2):
            t.rotate180()
        self.assertEqual(orig, str(t))

    def test_rotate270_full_rotation_1080degrees(self):
        t = tiles.Tile(self.tile1)
        orig = str(t)
        for i in range(4):
            t.rotate270()
        self.assertEqual(orig, str(t))

    def test_compareRotates_180degrees(self):
        t1 = tiles.Tile(self.tile1)
        t2 = tiles.Tile(self.tile1)
        for i in range(2):
            t1.rotate90()
            print(t1)
        t2.rotate180()
        self.assertEqual(str(t1), str(t2))

    def test_compareRotates_180degrees_flips(self):
        t1 = tiles.Tile(self.tile1)
        t2 = tiles.Tile(self.tile1)
        t1.flipHorizontal()
        t1.flipVertical()
        t2.rotate180()
        self.assertEqual(str(t1), str(t2))

    def test_compareRotates_270degrees_2steps(self):
        t1 = tiles.Tile(self.tile1)
        t2 = tiles.Tile(self.tile1)
        t1.rotate90()
        t1.rotate180()
        t2.rotate270()
        self.assertEqual(str(t1), str(t2))

    def test_compareRotates_270degrees_3steps(self):
        t1 = tiles.Tile(self.tile1)
        t2 = tiles.Tile(self.tile1)
        for i in range(3):
            t1.rotate90()
        t2.rotate270()
        self.assertEqual(str(t1), str(t2))

    def test_flipHorizontal_reversible(self):
        t = tiles.Tile(self.tile1)
        orig = str(t)
        for i in range(2):
            t.flipHorizontal()
        self.assertEqual(orig, str(t))

    def test_flipVertical_reversible(self):
        t = tiles.Tile(self.tile1)
        orig = str(t)
        for i in range(2):
            t.flipVertical()
        self.assertEqual(orig, str(t))

if __name__ == '__main__':
    unittest.main()
