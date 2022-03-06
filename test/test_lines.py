import unittest

from cartesian import lines


class TestLine(unittest.TestCase):
    def test_line_45_degrees_above(self):
        offset = 2
        points = [(i, i + offset) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_45_degrees_below(self):
        offset = 3
        points = [(i, i - offset) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_45_degrees_origin(self):
        points = [(i, i) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_135_degrees_above(self):
        offset = 4
        points = [(-i, i + offset) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_135_degrees_below(self):
        offset = 1
        points = [(-i, i - offset) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_135_degrees_origin(self):
        points = [(-i, i) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_horizontal_ltor_above(self):
        offset = 4
        points = [(i, offset) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_horizontal_ltor_below(self):
        offset = 2
        points = [(i, -offset) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_horizontal_ltor_origin(self):
        points = [(i, 0) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_vertical_up_left(self):
        offset = 3
        points = [(-offset, i) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_vertical_up_origin(self):
        points = [(0, i) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_line_vertical_up_right(self):
        offset = 9
        points = [(offset, i) for i in range(-5, 6)]
        # print(points)
        l = lines.Line(points[0], points[-1])
        self.assertEqual(points, list(l.points()))

    def test_monopoint_origin(self):
        point = (0, 0)
        l = lines.Line(point, point)
        self.assertEqual([point], list(l.points()))

    def test_monopoint_1_4(self):
        point = (1, 4)
        l = lines.Line(point, point)
        self.assertEqual([point], list(l.points()))

    def test_monopoint_neg2_3(self):
        point = (-2, 3)
        l = lines.Line(point, point)
        self.assertEqual([point], list(l.points()))

    def test_monopoint_neg3_neg2(self):
        point = (-3, -2)
        l = lines.Line(point, point)
        self.assertEqual([point], list(l.points()))

    def test_monopoint_5_neg1(self):
        point = (5, -1)
        l = lines.Line(point, point)
        self.assertEqual([point], list(l.points()))


def test_monopoint_neg2_3(self):
    point = (-2, 3)
    l = lines.Line(point, point)
    self.assertEqual([point], list(l.points()))


if __name__ == '__main__':
    unittest.main()
