"""
https://adventofcode.com/2020/day/25
"""
from encryptionkeys import encryptionkeys

if __name__ == '__main__':
    ekf = encryptionkeys.EncryptionKeyFinder(*[10441485, 1004920])
    print("Part 1: {}".format(ekf.encryptionKey))

