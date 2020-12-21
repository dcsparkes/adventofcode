from cartesian import cartesian
import unittest


class TestComplexTracker(unittest.TestCase):
    fInputTaxiA = "input2016_01a.txt"
    fTestTaxiA = "test2016_01a.txt"
    fTestTaxiB = "test2016_01b.txt"
    fTestTaxiC = "test2016_01c.txt"
    fTestTaxiD = "test2016_01d.txt"
    fInputShipA = "input2020_12a.txt"
    fTestShipA = "test2020_12a.txt"

    def test_ComplexTracker_fInputShipA(self):
        t = cartesian.ComplexTracker()
        t.readDirections(self.fInputShipA)
        self.assertEqual(582, t.getDistance())

    def test_ComplexTracker_fTestShipA(self):
        t = cartesian.ComplexTracker()
        t.readDirections(self.fTestShipA)
        self.assertEqual(25, t.getDistance())

    def test_TaxiTracker_fInputTaxiA(self):
        t = cartesian.TaxiTracker()
        t.readDirections(self.fInputTaxiA)
        self.assertEqual(231, t.getDistance())

    def test_TaxiTracker_fTestTaxiA(self):
        t = cartesian.TaxiTracker()
        t.readDirections(self.fTestTaxiA)
        self.assertEqual(5, t.getDistance())

    def test_TaxiTracker_fTestTaxiB(self):
        t = cartesian.TaxiTracker()
        t.readDirections(self.fTestTaxiB)
        self.assertEqual(2, t.getDistance())

    def test_TaxiTracker_fTestTaxiC(self):
        t = cartesian.TaxiTracker()
        t.readDirections(self.fTestTaxiC)
        self.assertEqual(12, t.getDistance())

    def test_TaxiTracker_fTestTaxiD(self):
        t = cartesian.TaxiTracker()
        t.readDirections(self.fTestTaxiD)
        self.assertEqual(8, t.getDistance())

    def test_TaxiTracker_task2_fInputTaxiA(self):
        t = cartesian.TaxiTracker()
        t.readDirections(self.fInputTaxiA)
        self.assertEqual(147, t.distanceManhattan(t.firstIntersection()))

    def test_TaxiTracker_task2_fTestTaxiA(self):
        t = cartesian.TaxiTracker()
        t.readDirections(self.fTestTaxiD)
        self.assertEqual(4, t.distanceManhattan(t.firstIntersection()))

    def test_WaypointTracker_fInputShipA(self):
        t = cartesian.WaypointTracker()
        t.readDirections(self.fInputShipA)
        self.assertEqual(582, t.getDistance())

    def test_WaypointTracker_fTestShipA(self):
        t = cartesian.WaypointTracker()
        t.readDirections(self.fTestShipA)
        self.assertEqual(286, t.getDistance())

if __name__ == '__main__':
    unittest.main()
