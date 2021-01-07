import hashlib
import itertools

class AdventCoinMiner():
    def solve(self, prefix, check="00000"):
        for i in itertools.count(1):
            hash = hashlib.md5("{}{}".format(prefix, i).encode('utf-8')).hexdigest()
            if check == hash[:len(check)]:
                return i

