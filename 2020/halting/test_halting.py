import halting
import logging
import unittest

class TestRisc(unittest.TestCase):
    def setUp(self):
        self.fInput = "input8.1.txt"
        self.fTest = "test8.1.txt"

    # def test_Risc_throughtrace_fInput(self):
    #     rProc = halting.Risc(self.fInput)
    #     rProc.throughtrace()
    #     self.assertEqual(1033, rProc.acc)

    def test_Risc_throughtrace_fTest(self):
        rProc = halting.Risc(self.fTest)
        rProc.throughtrace()
        self.assertEqual(8, rProc.acc)

    # def test_Risc_backtrace_fInput(self):
    #     rProc = halting.Risc(self.fInput)
    #     rProc.backtrace()
    #     self.assertEqual(1033, rProc.acc)
    #
    # def test_Risc_backtrace_fTest(self):
    #     rProc = halting.Risc(self.fTest)
    #     rProc.backtrace()
    #     self.assertEqual(8, rProc.acc)
    #
    # def test_Risc_haltPos_fInput(self):
    #     rProc = halting.Risc(self.fInput)
    #     self.assertEqual(626, rProc.haltPos)
    #
    # def test_Risc_haltPos_fTest(self):
    #     rProc = halting.Risc(self.fTest)
    #     self.assertEqual(9, rProc.haltPos)
    #
    # def test_Risc_termination_fInput(self):
    #     rProc = halting.Risc(self.fInput)
    #     self.assertEqual(1317, rProc.acc)
    #
    # def test_Risc_termination_fTest(self):
    #     rProc = halting.Risc(self.fTest)
    #     self.assertEqual(5, rProc.acc)

if __name__ == '__main__':
    logging.basicConfig(filename='test_halting.log', encoding='utf-8', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info("====================================================== NEW RUN ======================================================")
    unittest.main()
