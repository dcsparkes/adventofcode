import keypad
import unittest


class TestKeypad(unittest.TestCase):
    def test_init_default(self):
        kp = keypad.Keypad()
        kp.beep()
        self.assertEqual("5", kp.getCode())

    def test_init_default_keypad2(self):
        kp = keypad.Keypad(keypad.Keypad.pad2)
        kp.beep()
        self.assertEqual("5", kp.getCode())

    def test_inject(self):
        kp = keypad.Keypad()
        kp.inject("ULL\nRRDDD\nLURDL\nUUUUD")
        self.assertEqual("1985", kp.getCode())

    def test_inject_keypad2(self):
        kp = keypad.Keypad(keypad.Keypad.pad2)
        kp.inject("ULL\nRRDDD\nLURDL\nUUUUD")
        self.assertEqual("5DB3", kp.getCode())

    def test_input(self):
        kp = keypad.Keypad()
        kp.readFile("input2016_02a.txt")
        self.assertEqual("74921", kp.getCode())

    def test_input_keypad2(self):
        kp = keypad.Keypad(keypad.Keypad.pad2)
        kp.readFile("input2016_02a.txt")
        self.assertEqual("74921", kp.getCode())


if __name__ == '__main__':
    unittest.main()
