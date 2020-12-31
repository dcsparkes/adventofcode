"""
https://adventofcode.com/2020/day/20
"""
import unittest
from tiles import tiles


class TestDealer(unittest.TestCase):
    fInput = "input2020_20a.txt"
    fTest = "test2020_20a.txt"
    knownPuzzleSolution = [".#.#..#.##...#.##..#####", "###....#.#....#..#......", "##.##.###.#.#..######...",
                           "###.#####...#.#####.#..#", "##.#....#.##.####...#.##", "...########.#....#####.#",
                           "....#..#...##..#.#.###..", ".####...#..#.....#......", "#..#.##..#..###.#.##....",
                           "#.####..#.####.#.#.###..", "###.#.#...#.######.#..##", "#.####....##..########.#",
                           "##..##.#...#...#.#.#.#..", "...#..#..#.#.##..###.###", ".#.#....#.##.#...###.##.",
                           "###.#...#..#.##.######..", ".#.#.###.##.##.#..#.##..", ".####.###.#...###.#..#.#",
                           "..#.#..#..#.#.#.####.###", "#..####...#.#.#.###.###.", "#####..#####...###....##",
                           "#.##..#..#...#..####...#", ".#.###..##..##..####.##.", "...###...##...#...#..###"]

    serpentPattern = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

    def test_init_fTest_dims(self):
        d = tiles.Dealer(self.fTest)
        self.assertEqual(9, d.count)
        self.assertEqual((3, 3), d.dims)

    def test_init_corners_fInput(self):
        d = tiles.Dealer(self.fInput)
        self.assertEqual(45443966642567, d.calculateCornerMultiple())

    def test_init_corners_fTest(self):
        d = tiles.Dealer(self.fTest)
        self.assertEqual(20899048083289, d.calculateCornerMultiple())

    def test_assemblePuzzle_fTest_count(self):
        d = tiles.Dealer(self.fTest)
        d.assemblePuzzle()
        self.assertEqual(303, d.puzzle.countSymbol('#'))

    def test_assemblePuzzle_fTest_dims(self):
        d = tiles.Dealer(self.fTest)
        tileDims = d.tiles[0].dims
        puzzleDims = d.dims
        finalDims = ((tileDims[0] - 2) * puzzleDims[0], (tileDims[1] - 2) * puzzleDims[1])
        d.assemblePuzzle()
        self.assertEqual(finalDims, d.puzzle.dims)

    def test_assemblePuzzle_fInput_count(self):
        d = tiles.Dealer(self.fInput)
        d.assemblePuzzle()
        self.assertEqual(1922, d.puzzle.countSymbol('#'))

    def test_assemblePuzzle_fInput_dims(self):
        d = tiles.Dealer(self.fInput)
        tileDims = d.tiles[0].dims
        puzzleDims = d.dims
        finalDims = ((tileDims[0] - 2) * puzzleDims[0], (tileDims[1] - 2) * puzzleDims[1])
        d.assemblePuzzle()
        self.assertEqual(finalDims, d.puzzle.dims)

    def test_assemblePuzzle_fTest_knownGoodAssembly(self):
        d = tiles.Dealer(self.fTest)
        d.assemblePuzzle()
        matched = False
        for t in d.puzzle.spin():
            matched |= t.tile == self.knownPuzzleSolution
        self.assertTrue(matched)

    def test_findSerpents_fTest_count(self):
        d = tiles.Dealer(self.fTest)
        d.assemblePuzzle()
        self.assertEqual(2, len(d.findSerpents()))

    def test_findSerpents_fInput_count(self):
        d = tiles.Dealer(self.fInput)
        d.assemblePuzzle()
        self.assertEqual(21, len(d.findSerpents()))




class TestTile(unittest.TestCase):
    tile1 = ["Tile 1:", "..#", ".##", "..#"]
    t1Sides = [(1, 4), (7, 7), (1, 4), (0, 0)]

    tile2 = ["Tile 2:", "...#", "..##", "###.", ".###"]
    t2Sides = [(1, 8), (11, 13), (7, 14), (2, 4)]
    serpentsLocated = [".####...#####..#...###..",
                       "#####..#..#.#.####..#.#.",
                       ".#.#...#.###...#.##.O#..",
                       "#.O.##.OO#.#.OO.##.OOO##",
                       "..#O.#O#.O##O..O.#O##.##",
                       "...#.#..##.##...#..#..##",
                       "#.##.#..#.#..#..##.#.#..",
                       ".###.##.....#...###.#...",
                       "#.####.#.#....##.#..#.#.",
                       "##...#..#....#..#...####",
                       "..#.##...###..#.#####..#",
                       "....#.##.#.#####....#...",
                       "..##.##.###.....#.##..#.",
                       "#...#...###..####....##.",
                       ".#.##...#.##.#.#.###...#",
                       "#.###.#..####...##..#...",
                       "#.###...#.##...#.##O###.",
                       ".O##.#OO.###OO##..OOO##.",
                       "..O#.O..O..O.#O##O##.###",
                       "#.#..##.########..#..##.",
                       "#.#####..#.#...##..#....",
                       "#....##..#.#########..##",
                       "#...#.....#..##...###.##",
                       "#..###....##.#...##.##.#"]

    knownPuzzleSolutionOriented = [".####...#####..#...###..",
                                   "#####..#..#.#.####..#.#.",
                                   ".#.#...#.###...#.##.##..",
                                   "#.#.##.###.#.##.##.#####",
                                   "..##.###.####..#.####.##",
                                   "...#.#..##.##...#..#..##",
                                   "#.##.#..#.#..#..##.#.#..",
                                   ".###.##.....#...###.#...",
                                   "#.####.#.#....##.#..#.#.",
                                   "##...#..#....#..#...####",
                                   "..#.##...###..#.#####..#",
                                   "....#.##.#.#####....#...",
                                   "..##.##.###.....#.##..#.",
                                   "#...#...###..####....##.",
                                   ".#.##...#.##.#.#.###...#",
                                   "#.###.#..####...##..#...",
                                   "#.###...#.##...#.######.",
                                   ".###.###.#######..#####.",
                                   "..##.#..#..#.#######.###",
                                   "#.#..##.########..#..##.",
                                   "#.#####..#.#...##..#....",
                                   "#....##..#.#########..##",
                                   "#...#.....#..##...###.##",
                                   "#..###....##.#...##.##.#"]

    knownPuzzleSolutionUnoriented = [".#.#..#.##...#.##..#####",
                                     "###....#.#....#..#......",
                                     "##.##.###.#.#..######...",
                                     "###.#####...#.#####.#..#",
                                     "##.#....#.##.####...#.##",
                                     "...########.#....#####.#",
                                     "....#..#...##..#.#.###..",
                                     ".####...#..#.....#......",
                                     "#..#.##..#..###.#.##....",
                                     "#.####..#.####.#.#.###..",
                                     "###.#.#...#.######.#..##",
                                     "#.####....##..########.#",
                                     "##..##.#...#...#.#.#.#..",
                                     "...#..#..#.#.##..###.###",
                                     ".#.#....#.##.#...###.##.",
                                     "###.#...#..#.##.######..",
                                     ".#.#.###.##.##.#..#.##..",
                                     ".####.###.#...###.#..#.#",
                                     "..#.#..#..#.#.#.####.###",
                                     "#..####...#.#.#.###.###.",
                                     "#####..#####...###....##",
                                     "#.##..#..#...#..####...#",
                                     ".#.###..##..##..####.##.",
                                     "...###...##...#...#..###"]

    serpentPattern = ["                  # ",
                      "#    ##    ##    ###",
                      " #  #  #  #  #  #   "]

    def test_init_sideID_calculation_3x3(self):
        t = tiles.Tile(self.tile1)
        self.assertEqual(self.t1Sides, t.sideIDs)

    def test_init_sideID_calculation_4x4(self):
        t = tiles.Tile(self.tile2)
        self.assertEqual(self.t2Sides, t.sideIDs)

    def test_count(self):
        buffer = ["0"]
        buffer.extend(self.knownPuzzleSolutionOriented)
        tile = tiles.Tile(buffer)
        self.assertEqual(303, tile.countSymbol('#'))

    def test_findPattern_knownGoodAssembly_oriented_count(self):
        buffer = ["0"]
        buffer.extend(self.knownPuzzleSolutionOriented)
        tile = tiles.Tile(buffer)
        matches = [m for m in tile._findPatternMatches(self.serpentPattern)]
        self.assertTrue(2, len(matches))

    def test_findPattern_knownGoodAssembly_unoriented_count(self):
        buffer = ["0"]
        buffer.extend(self.knownPuzzleSolutionUnoriented)
        tile = tiles.Tile(buffer)
        matches = [m for m in tile._findPatternMatches(self.serpentPattern)]
        self.assertTrue(2, len(matches))

    def test_findPatternMatches_knownGoodAssembly_count(self):
        buffer = ["0"]
        buffer.extend(self.knownPuzzleSolutionOriented)
        tile = tiles.Tile(buffer)
        matches = [m for m in tile._findPatternMatches(self.serpentPattern)]
        self.assertTrue(2, len(matches))

    def test_findPatternMatches_knownGoodAssembly_match(self):
        buffer = ["0"]
        buffer.extend(self.knownPuzzleSolutionOriented)
        tile = tiles.Tile(buffer)
        matches = [m for m in tile._findPatternMatches(self.serpentPattern)]
        self.assertEqual(set([(2, 2), (1, 16)]), set(matches))

    def test_patternMatch_knownGoodAssembly_pos1(self):
        buffer = ["0"]
        buffer.extend(self.knownPuzzleSolutionOriented)
        tile = tiles.Tile(buffer)
        self.assertTrue(tile._patternMatch((2, 2), self.serpentPattern))

    def test_patternMatch_knownGoodAssembly_pos2(self):
        buffer = ["0"]
        buffer.extend(self.knownPuzzleSolutionOriented)
        tile = tiles.Tile(buffer)
        self.assertTrue(tile._patternMatch((1, 16), self.serpentPattern))

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

    def test_rotate90_edgeIDs_3x3(self):
        t = tiles.Tile(self.tile1)
        t.rotate90()
        expected = [self.t1Sides[3], self.t1Sides[0], self.t1Sides[1], self.t1Sides[2]]
        self.assertEqual(expected, t.sideIDs)

    def test_rotate90_edgeIDs_4x4(self):
        t = tiles.Tile(self.tile2)
        t.rotate90()
        expected = [self.t2Sides[3], self.t2Sides[0], self.t2Sides[1], self.t2Sides[2]]
        self.assertEqual(expected, t.sideIDs)

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

    def test_rotate180_edgeIDs_3x3(self):
        t = tiles.Tile(self.tile1)
        t.rotate180()
        expected = [self.t1Sides[2], self.t1Sides[3], self.t1Sides[0], self.t1Sides[1]]
        self.assertEqual(expected, t.sideIDs)

    def test_rotate180_edgeIDs_4x4(self):
        t = tiles.Tile(self.tile2)
        t.rotate180()
        expected = [self.t2Sides[2], self.t2Sides[3], self.t2Sides[0], self.t2Sides[1]]
        self.assertEqual(expected, t.sideIDs)

    def test_rotate180_full_rotation_360degrees(self):
        t = tiles.Tile(self.tile1)
        orig = str(t)
        for i in range(2):
            t.rotate180()
        self.assertEqual(orig, str(t))

    def test_rotate270_edgeIDs_3x3(self):
        t = tiles.Tile(self.tile1)
        t.rotate270()
        expected = [self.t1Sides[1], self.t1Sides[2], self.t1Sides[3], self.t1Sides[0]]
        self.assertEqual(expected, t.sideIDs)

    def test_rotate270_edgeIDs_4x4(self):
        t = tiles.Tile(self.tile2)
        t.rotate270()
        expected = [self.t2Sides[1], self.t2Sides[2], self.t2Sides[3], self.t2Sides[0]]
        self.assertEqual(expected, t.sideIDs)

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
            # print(t1)
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

    def test_flipHorizontal_edgeIDs_3x3(self):
        t = tiles.Tile(self.tile1)
        t.flipHorizontal()
        expected = [self.t1Sides[0], self.t1Sides[3], self.t1Sides[2], self.t1Sides[1]]
        self.assertEqual(expected, t.sideIDs)

    def test_flipHorizontal_edgeIDs_4x4(self):
        t = tiles.Tile(self.tile2)
        t.flipHorizontal()
        expected = [self.t2Sides[0], self.t2Sides[3], self.t2Sides[2], self.t2Sides[1]]
        self.assertEqual(expected, t.sideIDs)

    def test_flipHorizontal_reversible(self):
        t = tiles.Tile(self.tile1)
        orig = str(t)
        for i in range(2):
            t.flipHorizontal()
        self.assertEqual(orig, str(t))

    def test_flipVertical_edgeIDs_3x3(self):
        t = tiles.Tile(self.tile1)
        t.flipVertical()
        expected = [self.t1Sides[2], self.t1Sides[1], self.t1Sides[0], self.t1Sides[3]]
        self.assertEqual(expected, t.sideIDs)

    def test_flipVertical_edgeIDs_4x4(self):
        t = tiles.Tile(self.tile2)
        t.flipVertical()
        expected = [self.t2Sides[2], self.t2Sides[1], self.t2Sides[0], self.t2Sides[3]]
        self.assertEqual(expected, t.sideIDs)

    def test_flipVertical_reversible(self):
        t = tiles.Tile(self.tile1)
        orig = str(t)
        for i in range(2):
            t.flipVertical()
        self.assertEqual(orig, str(t))


if __name__ == '__main__':
    unittest.main()
