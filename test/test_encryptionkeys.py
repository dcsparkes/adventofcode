from encryptionkeys import encryptionkeys
import unittest


class TestEncryptionKeyFinder(unittest.TestCase):
    keysPublic_test = [5764801, 17807724]
    keysPublic_input = [10441485, 1004920]

    def test_init(self):
        ekf = encryptionkeys.EncryptionKeyFinder(*self.keysPublic_test)
        self.assertEqual((8, 11), ekf.loopSizes)

    def test_calculateEncryptionKey_test(self):
        ekf = encryptionkeys.EncryptionKeyFinder(*self.keysPublic_test)
        self.assertEqual(14897079, ekf.encryptionKey)

    def test_calculateEncryptionKey_input(self):
        ekf = encryptionkeys.EncryptionKeyFinder(*self.keysPublic_input)
        self.assertEqual(14897079, ekf.encryptionKey)

class TestTransformSequence(unittest.TestCase):
    keyPublic1 = 5764801
    loopSize1 = 8
    keyPublic2 = 17807724
    loopSize2 = 11
    encryptionKey = 14897079

    def test_iter_keyPublic1_knownLoopSize(self):
        ts = encryptionkeys.TransformSequence(subject=7)
        for i in range(self.loopSize1):
            key = next(ts)
        self.assertEqual(self.keyPublic1, key)

    def test_iter_keyPublic2_knownLoopSize(self):
        ts = encryptionkeys.TransformSequence(subject=7)
        for i in range(self.loopSize2):
            key = next(ts)
        self.assertEqual(self.keyPublic2, key)

    def test_iter_encryptionkeys_1_2(self):
        ts = encryptionkeys.TransformSequence(subject=self.keyPublic1)
        for i in range(self.loopSize2):
            key = next(ts)
        self.assertEqual(self.encryptionKey, key)

    def test_iter_encryptionkeys_2_1(self):
        ts = encryptionkeys.TransformSequence(subject=self.keyPublic2)
        for i in range(self.loopSize1):
            key = next(ts)
        self.assertEqual(self.encryptionKey, key)

    def test_iter_encryptionkeysMatch_knownLoopSizes(self):
        ts1 = encryptionkeys.TransformSequence(subject=self.keyPublic1)
        ts2 = encryptionkeys.TransformSequence(subject=self.keyPublic2)
        for i in range(self.loopSize2):
            key1 = next(ts1)
        for i in range(self.loopSize1):
            key2 = next(ts2)
        self.assertEqual(key1, key2)


if __name__ == '__main__':
    unittest.main()
