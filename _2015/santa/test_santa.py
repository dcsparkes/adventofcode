import santa
import unittest

class TestSanta(unittest.TestCase):
    def setUp(self):
        self.fInput = "input3.1.txt"
        self.fTest1a = "test1a.txt"
        self.fTest1b = "test1b.txt"
        self.fTest2 = "test2.txt"
        self.fTest3 = "test3.txt"
        self.elf = santa.Dispatcher() # Elf on a self
        self.elf2 = santa.Dispatcher(2)


    def test_Dispatcher_init_default(self):
        # Santa delivers to start position
        self.assertEqual(1, self.elf.countRecipients())

    def test_Dispatcher_init_variablePools(self):
        for i in range(1, 4):
            # All Santas start in same position
            self.assertEqual(1, santa.Dispatcher(i).countRecipients(), "iteration: {}".format(i))

    def test_Dispatcher_init_negativePool(self):
        with self.assertRaises(ValueError):
            santa.Dispatcher(-1)

    def test_Dispatcher_init_zeroPool(self):
        with self.assertRaises(ValueError):
            santa.Dispatcher(0)

    def test_Dispatcher_convertArrowToComplex_eastWest(self):
        self.assertEqual(0, self.elf.convertArrowToComplex('<') + self.elf.convertArrowToComplex('>'))

    def test_Dispatcher_convertArrowToComplex_northSouth(self):
        self.assertEqual(0, self.elf.convertArrowToComplex('^') + self.elf.convertArrowToComplex('v'))

    def test_Dispatcher_fInput_defaultPool_defaultPos(self):
        self.elf.dispatchCycle(self.fInput)
        self.assertEqual(2565, self.elf.countRecipients())

    def test_Dispatcher_ftest1a_defaultPool_defaultPos(self):
        self.elf.dispatchCycle(self.fTest1a)
        self.assertEqual(2, self.elf.countRecipients())

    def test_Dispatcher_ftest2_defaultPool_defaultPos(self):
        self.elf.dispatchCycle(self.fTest2)
        self.assertEqual(4, self.elf.countRecipients())

    def test_Dispatcher_ftest3_defaultPool_defaultPos(self):
        self.elf.dispatchCycle(self.fTest3)
        self.assertEqual(2, self.elf.countRecipients())

    def test_Dispatcher_fInput_pool2_defaultPos(self):
        self.elf2.dispatchCycle(self.fInput)
        self.assertEqual(2639, self.elf2.countRecipients())

    def test_Dispatcher_ftest1a_pool2_defaultPos(self):
        self.elf2.dispatchCycle(self.fTest1a)
        self.assertEqual(2, self.elf2.countRecipients())

    def test_Dispatcher_ftest1b_pool2_defaultPos(self):
        self.elf2.dispatchCycle(self.fTest1b)
        self.assertEqual(3, self.elf2.countRecipients())

    def test_Dispatcher_ftest2_pool2_defaultPos(self):
        self.elf2.dispatchCycle(self.fTest2)
        self.assertEqual(3, self.elf2.countRecipients())

    def test_Dispatcher_ftest3_pool2_defaultPos(self):
        self.elf2.dispatchCycle(self.fTest3)
        self.assertEqual(11, self.elf2.countRecipients())

    def test_RecipientTracker_init(self):
        rt = santa.RecipientTracker()
        self.assertEqual(0, rt.countRecipients())

    def test_RecipientTracker_countRecipients_nonRepeatDeliveries_north(self):
        pos = 5 - 9j
        move = 1 - 0j
        rt = santa.RecipientTracker()
        for i in range(1, 11):
            rt.registerDelivery(pos)
            self.assertEqual(i, rt.countRecipients(), "start: {} iteration: {}".format(pos, i))
            pos += move

    def test_RecipientTracker_countRecipients_nonRepeatDeliveries_northWest(self):
        pos = 9 + 4j
        move = 1 + 1j
        rt = santa.RecipientTracker()
        for i in range(1, 11):
            rt.registerDelivery(pos)
            self.assertEqual(i, rt.countRecipients(), "start: {} iteration: {}".format(pos, i))
            pos += move

    def test_RecipientTracker_countRecipients_nonRepeatDeliveries_West(self):
        pos = -9 + 2j
        move = 0 + 1j
        rt = santa.RecipientTracker()
        for i in range(1, 11):
            rt.registerDelivery(pos)
            self.assertEqual(i, rt.countRecipients(), "start: {} iteration: {}".format(pos, i))
            pos += move

    def test_RecipientTracker_countRecipients_nonRepeatDeliveries_southWest(self):
        pos = -9 + 9j
        move = -1 + 1j
        rt = santa.RecipientTracker()
        for i in range(1, 11):
            rt.registerDelivery(pos)
            self.assertEqual(i, rt.countRecipients(), "start: {} iteration: {}".format(pos, i))
            pos += move

    def test_RecipientTracker_countRecipients_nonRepeatDeliveries_south(self):
        pos = 2 - 9j
        move = -1 + 0j
        rt = santa.RecipientTracker()
        for i in range(1, 11):
            rt.registerDelivery(pos)
            self.assertEqual(i, rt.countRecipients(), "start: {} iteration: {}".format(pos, i))
            pos += move

    def test_RecipientTracker_countRecipients_nonRepeatDeliveries_southEast(self):
        pos = 7 + 5j
        move = -1 - 1j
        rt = santa.RecipientTracker()
        for i in range(1, 11):
            rt.registerDelivery(pos)
            self.assertEqual(i, rt.countRecipients(), "start: {} iteration: {}".format(pos, i))
            pos += move

    def test_RecipientTracker_countRecipients_nonRepeatDeliveries_East(self):
        pos = 7 + 0j
        move = 0 - 1j
        rt = santa.RecipientTracker()
        for i in range(1, 11):
            rt.registerDelivery(pos)
            self.assertEqual(i, rt.countRecipients(), "start: {} iteration: {}".format(pos, i))
            pos += move

    def test_RecipientTracker_countRecipients_nonRepeatDeliveries_northEast(self):
        pos = 6 + 4j
        move = 1 - 1j
        rt = santa.RecipientTracker()
        for i in range(1, 11):
            rt.registerDelivery(pos)
            self.assertEqual(i, rt.countRecipients(), "start: {} iteration: {}".format(pos, i))
            pos += move

    def test_RecipientTracker_countRecipients_repeatDeliveries_cyclic(self):
        poss = [4 + 1j, 3 - 3j, 4 - 6j, 10 - 3j]

        rt = santa.RecipientTracker()
        for i in range(5):
            for pos in poss:
                rt.registerDelivery(pos)
            self.assertEqual(len(poss), rt.countRecipients(), "iteration: {}".format(i))

    def test_RecipientTracker_countRecipients_repeatDeliveries_grid(self):
        size = 5
        poss = [complex(a, b) for a in range(-size, size + 1) for b in range (-size, size + 1)]

        rt = santa.RecipientTracker()
        for i in range(5):
            for pos in poss:
                rt.registerDelivery(pos)
            self.assertEqual(len(poss), rt.countRecipients(), "iteration: {}".format(i))

    # Original implementation functions
    def test_houseCount_input(self):
        self.assertEqual(2565, santa.houseCount(self.fInput))

    def test_houseCount_test1(self):
        self.assertEqual(2, santa.houseCount(self.fTest1a))

    def test_houseCount_test2(self):
        self.assertEqual(4, santa.houseCount(self.fTest2))

    def test_houseCount_test3(self):
        self.assertEqual(2, santa.houseCount(self.fTest3))

if __name__ == '__main__':
    unittest.main()
