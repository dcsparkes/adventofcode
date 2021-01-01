"""
https://adventofcode.com/2020/day/14
"""
import unittest
from base import base


class MemBank_v1:
    def __init__(self, fileName=None):
        self.mem = {}

        if fileName:
            self.readInput(fileName)

    def applyMasks(self, masks, value):
        retVal = value
        if masks:
            maskAnd, maskOr = masks
            retVal &= maskAnd
            retVal |= maskOr
        return retVal

    def createMasks(self, definition):
        """
        :param definition: Ternary string 0, 1, X
        :return: Tuple: (maskAnd: int, maskOr: int)
        """
        maskAnd = []
        maskOr = []
        for bit in definition:
            if bit == 'X':
                maskAnd.append('1')
                maskOr.append('0')
            elif bit == '1' or bit == '0':
                maskAnd.append(bit)
                maskOr.append(bit)
        return (int(''.join(maskAnd), 2), int(''.join(maskOr), 2))

    def readInput(self, fileName):
        masksCurrent = None

        for line in base.getInputLines(fileName):
            if (line):
                prefix, suffix = line.split(' = ')
                if prefix == "mask":
                    masksCurrent = self.createMasks(suffix)
                else:
                    self.write(int(prefix.strip('me[] ')), suffix, masksCurrent)

    def total(self):
        # print(self.mem)
        return sum(self.mem.values())

    def write(self, address, value, masks):
        self.mem[address] = self.applyMasks(masks, int(value))


class MemBank_v2(MemBank_v1):
    def createMasks(self, definition):
        maskOr = []
        masksXor = [[]]
        for bit in definition:
            if bit == 'X':
                maskOr.append('0')
                for i in range(len(masksXor)):
                    masksXor.append(masksXor[i][:])
                    masksXor[i].append('0')
                    masksXor[-1].append('1')

            elif bit == '1' or bit == '0':
                maskOr.append(bit)
                for mask in masksXor:
                    mask.append('0')

        return (int(''.join(maskOr), 2), [int(''.join(mask), 2) for mask in masksXor])

    def applyMasks(self, masks, address):
        retVal = int(address)
        if masks:
            maskOr = masks[0]
            masksXor = masks[1]
            for m in masksXor:
                # print("{}: {}: {}".format(type(address), type(maskOr), type(m)))
                # print("{} ^ {} | {} = {}".format(m, address, maskOr, m ^ address | maskOr))
                yield m ^ address | maskOr

    def write(self, address, value, masks):
        for addr in self.applyMasks(masks, address):
            # print(addr)
            self.mem[addr] = int(value)


class TestMemBank_v2(unittest.TestCase):
    fInput1a = "input2020_14a.txt"
    fTest1b = "test2020_14b.txt"

    def test_MemBank_fInput1a(self):
        mb = MemBank_v2(self.fInput1a)
        total = mb.total()
        print("Part 2: {}".format(total))
        self.assertEqual(5579916171823, total)

    def test_MemBank_fTest1b(self):
        mb = MemBank_v2(self.fTest1b)
        self.assertEqual(208, mb.total())

    def test_MemBank_createMasks_countSanityCheck(self):
        mb = MemBank_v2()
        mask = ['0', '1'] * 18
        for i in range(13):
            if i:
                mask[3 * i - 2] = 'X'
            # print(''.join(mask))
            masks = mb.createMasks(''.join(mask))
            self.assertEqual(2 ** i, len(masks[1]), "{}:{}".format(i, mask))

    def test_MemBank_createMasks_tupleSanityCheck(self):
        mb = MemBank_v2()
        masks = mb.createMasks("0" * 36)
        self.assertEqual(2, len(masks))


class TestMemBank_v1(unittest.TestCase):
    fInput1a = "input2020_14a.txt"
    fTest1a = "test2020_14a.txt"

    def test_MemBank_fInput1a(self):
        mb = MemBank_v1(self.fInput1a)
        total = mb.total()
        print("Part 1: {}".format(total))
        self.assertEqual(13727901897109, total)

    def test_MemBank_fTest1a(self):
        mb = MemBank_v1(self.fTest1a)
        self.assertEqual(165, mb.total())

    def test_createMask_ints_16bit(self):
        mb = MemBank_v1()
        bits = 16
        for i in range(2 ** bits):
            binary = format(i, '0{}b'.format(bits))
            # print(binary)
            self.assertEqual((i, i), mb.createMasks(binary), "i = {}".format(i))

    def test_createMask_ints_0asX_16bit(self):
        mb = MemBank_v1()
        bits = 16
        for i in range(2 ** bits):
            binary = format(i, '0{}b'.format(bits)).replace('0', 'X')
            # print(binary)
            self.assertEqual((65535, i), mb.createMasks(binary), "i = {}".format(i))

    def test_createMask_ints_1asX_16bit(self):
        mb = MemBank_v1()
        bits = 16
        for i in range(2 ** bits):
            binary = format(i, '0{}b'.format(bits)).replace('1', 'X')
            # print(binary)
            self.assertEqual((i, 0), mb.createMasks(binary), "i = {}".format(i))


if __name__ == '__main__':
    unittest.main()
