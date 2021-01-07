import triangles
import unittest


class TestTriangles(unittest.TestCase):
    def test_pivot(self):
        ts = triangles.Triangles()
        ts.readFile("input2016_03a.txt")
        ts.pivot()
        self.assertEqual(None, ts.count())

    def test_readTriangles(self):
        ts = triangles.Triangles()
        ts.readFile("input2016_03a.txt")
        self.assertEqual(917, ts.count())

    def test_validateTriangle_invalid(self):
        self.assertEqual(False, triangles.Triangles._validateTriangle([5, 10, 25]))

    def test_validateTriangle_invalid_unsorted(self):
        self.assertEqual(False, triangles.Triangles._validateTriangle([10, 25, 5]))


if __name__ == '__main__':
    unittest.main()
