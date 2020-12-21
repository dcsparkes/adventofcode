import lightGrid
import logging
import unittest


class TestLightGrid(unittest.TestCase):
    def setUp(self) -> None:
        self.fInput = "input2015_06a.txt"
        self.fTesta = "test2015_06a.txt"
        self.fTestb = "test2015_06b.txt"
    ################################################
    # Internal functions                           #
    ################################################
    def test_LightGrid_init_0D(self):
        lg = lightGrid.LightGrid([])
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_init_v2_0D(self):
        lg = lightGrid.LightGrid([], version=2)
        self.assertEqual(0, lg.totalSum())

    def test_LightGrid_init_1D_string(self):
        lg = lightGrid.LightGrid("30")
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_init_asymmetricGrowing_byReference(self):
        lg = lightGrid.LightGrid((2, 3, 4))
        lg.grid[1][2][3] = True
        self.assertEqual(True, lg.grid[1][2][3])

    def test_LightGrid_init_asymmetricGrowing_bySize(self):
        lg = lightGrid.LightGrid((2, 3, 4))
        self.assertEqual([False] * 4, lg.grid[0][0])

    def test_LightGrid_init_asymmetricShrinking_byReference(self):
        lg = lightGrid.LightGrid((4, 3, 2))
        lg.grid[3][2][1] = True
        self.assertEqual(True, lg.grid[3][2][1])

    def test_LightGrid_init_asymmetricShrinking_bySize(self):
        lg = lightGrid.LightGrid((4, 3, 2))
        self.assertEqual([False] * 2, lg.grid[0][0])

    def test_LightGrid_init_default(self):
        lg = lightGrid.LightGrid()
        self.assertEqual((1000, 1000), lg.gridSize)

    def test_LightGrid_init_v2_default(self):
        lg = lightGrid.LightGrid(version=2)
        self.assertEqual((1000, 1000), lg.gridSize)

    def test_LightGrid_init_onCount(self):
        lg = lightGrid.LightGrid()
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_extrudeCorners_2D_extrude1D(self):
        lg = lightGrid.LightGrid((5, 5))
        c1, c2 = lg._extrudeCorners((3,), (4,))
        self.assertEqual((3, 0), c1, "Near Corner")
        self.assertEqual((4, 4), c2, "Far Corner")

    def test_LightGrid_extrudeCorners_2D_truncate3D(self):
        lg = lightGrid.LightGrid((5, 5))
        c1, c2 = lg._extrudeCorners((3, 3, 3), (4, 4, 4))
        self.assertEqual((3, 3), c1, "Near Corner")
        self.assertEqual((4, 4), c2, "Far Corner")

    def test_LightGrid_extrudeCorners_3D_extrude1D(self):
        lg = lightGrid.LightGrid((5, 5, 5))
        c1, c2 = lg._extrudeCorners((3,), (4,))
        self.assertEqual((3, 0, 0), c1, "Near Corner")
        self.assertEqual((4, 4, 4), c2, "Far Corner")

    def test_LightGrid_extrudeCorners_3D_extrude2D(self):
        lg = lightGrid.LightGrid((5, 5, 5))
        c1, c2 = lg._extrudeCorners((3, 1), (4, 2))
        self.assertEqual((3, 1, 0), c1, "Near Corner")
        self.assertEqual((4, 2, 4), c2, "Far Corner")

    def test_LightGrid_extrudeCorners_2D_truncateProtrudingX(self):
        lg = lightGrid.LightGrid((5, 5))
        c1, c2 = lg._extrudeCorners((-1, 2), (5, 2))
        self.assertEqual((0, 2), c1, "Near Corner")
        self.assertEqual((4, 2), c2, "Far Corner")

    def test_LightGrid_extrudeCorners_2D_truncateProtrudingY(self):
        lg = lightGrid.LightGrid((5, 5))
        c1, c2 = lg._extrudeCorners((2, -1), (2, 5))
        self.assertEqual((2, 0), c1, "Near Corner")
        self.assertEqual((2, 4), c2, "Far Corner")

    ################################################
    # External functions                           #
    ################################################
    # def test_LightGrid_runInstructions_fInput(self):
    #     lg = lightGrid.LightGrid()
    #     lg.readInstructions(self.fInput)
    #     self.assertEqual(377891, lg.onCount())

    def test_LightGrid_runInstructions_fTesta(self):
        lg = lightGrid.LightGrid()
        lg.readInstructions(self.fTesta)
        self.assertEqual(998996 , lg.onCount())

    def test_LightGrid_runInstructions_v2_fInput(self):
        lg = lightGrid.LightGrid(version=2)
        lg.readInstructions(self.fInput)
        self.assertEqual(1, lg.totalSum())

    def test_LightGrid_runInstructions_fTestb(self):
        lg = lightGrid.LightGrid(version=2)
        lg.readInstructions(self.fTestb)
        self.assertEqual(2000001, lg.totalSum())


    def test_LightGrid_toggle_1D_allLightDoubleToggle(self):
        lg = lightGrid.LightGrid((5,))
        lg.toggle((0,), (4,))
        lg.toggle((0,), (4,))
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_toggle_1D_allLightOn(self):
        lg = lightGrid.LightGrid((5,))
        lg.toggle((0,), (4,))
        self.assertEqual(5, lg.onCount())

    def test_LightGrid_toggle_1D_oneLightDoubleToggle(self):
        lg = lightGrid.LightGrid((5,))
        lg.toggle((3,), (3,))
        lg.toggle((3,), (3,))
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_toggle_1D_oneLightOn(self):
        lg = lightGrid.LightGrid((5,))
        lg.toggle((3,), (3,))
        self.assertEqual(1, lg.onCount())

    def test_LightGrid_toggle_1D_twoLights(self):
        lg = lightGrid.LightGrid((5,))
        lg.toggle((1,), (2,))
        self.assertEqual(2, lg.onCount())

    def test_LightGrid_toggle_1D_twoLightsDoubleToggle(self):
        lg = lightGrid.LightGrid((5,))
        lg.toggle((1,), (2,))
        lg.toggle((1,), (2,))
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_toggle_2D_oneColumn(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.toggle((0, 2), (4, 2))
        self.assertEqual(5, lg.onCount())

    def test_LightGrid_toggle_2D_oneLightDoubleToggle(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.toggle((3, 1), (3, 1))
        lg.toggle((3, 1), (3, 1))
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_toggle_2D_oneColumnDoubleToggle(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.toggle((0, 2), (4, 2))
        lg.toggle((0, 2), (4, 2))
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_toggle_2D_oneRow(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.toggle((4, 0), (4, 4))
        lg.toggle((4, 0), (4, 4))
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_toggle_2D_oneLight(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.toggle((3, 1), (3, 1))
        self.assertEqual(1, lg.onCount())

    def test_LightGrid_toggle_2D_oneRow(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.toggle((4, 0), (4, 4))
        self.assertEqual(5, lg.onCount())

    def test_LightGrid_turnOn_1D_allLights(self):
        lg = lightGrid.LightGrid((5,))
        lg.turnOn((0,), (4,))
        self.assertEqual(5, lg.onCount())

    def test_LightGrid_turnOn_1D_allLights_emptyTuples(self):
        lg = lightGrid.LightGrid((5,))
        lg.turnOn((), ())
        self.assertEqual(5, lg.onCount())

    def test_LightGrid_turnOn_1D_allLights_sequential(self):
        dimSize = 5
        lg = lightGrid.LightGrid((dimSize,))
        for i in range(dimSize):
            lg.turnOn((i,), (i,))
            self.assertEqual(i + 1, lg.onCount(), i + 1)

    def test_LightGrid_turnOn_1D_oneLight(self):
        dimSize = 5
        lg = lightGrid.LightGrid((dimSize,))
        lg.turnOn((3,), (3,))
        self.assertEqual(1, lg.onCount())

    def test_LightGrid_turnOn_1D_twoLights(self):
        lg = lightGrid.LightGrid((5,))
        lg.turnOn((1,), (2,))
        self.assertEqual(2, lg.onCount())

    def test_LightGrid_turnOn_2D_allLight(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.turnOn((0, 0), (4, 4))
        self.assertEqual(25, lg.onCount())

    def test_LightGrid_turnOn_2D_allLight_emptyTuples(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.turnOn((), ())
        self.assertEqual(25, lg.onCount())

    def test_LightGrid_turnOn_2D_allLights_sequential(self):
        dimSizes = (3, 4)
        lg = lightGrid.LightGrid(dimSizes)
        for i in range(dimSizes[0]):
            for k in range(dimSizes[1]):
                lg.turnOn((i, k), (i, k))
                self.assertEqual((i * dimSizes[1] + k + 1), lg.onCount(), "i:{}, k:{}".format(i, k))

    def test_LightGrid_turnOn_2D_oneColumnOn(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.turnOn((0, 2), (4, 2))
        self.assertEqual(5, lg.onCount())

    def test_LightGrid_turnOn_2D_oneLightOn(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.turnOn((3, 1), (3, 1))
        self.assertEqual(1, lg.onCount())

    def test_LightGrid_turnOn_2D_oneRowOn(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.turnOn((4, 0), (4, 4))
        self.assertEqual(5, lg.onCount())

    def test_LightGrid_turnOn_2D_outOfRange_tooHighX(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.turnOn((5, 0), (5, 4))
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_turnOn_2D_outOfRange_tooHighY(self):
        lg = lightGrid.LightGrid((5, 5))
        lg.turnOn((2, 5), (3, 5))
        self.assertEqual(0, lg.onCount())

    def test_LightGrid_turnOn_3D_allLight(self):
        lg = lightGrid.LightGrid((4, 4, 4))
        lg.turnOn((0, 0, 0), (4, 4, 4))
        self.assertEqual(64, lg.onCount())

    def test_LightGrid_turnOn_3D_allLight_emptyTuples(self):
        lg = lightGrid.LightGrid((5, 5, 5))
        lg.turnOn((), ())
        self.assertEqual(125, lg.onCount())



if __name__ == '__main__':
    logging.basicConfig(filename='test_lightGrid.log', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(
        "====================================================== NEW RUN ======================================================")
    unittest.main()
