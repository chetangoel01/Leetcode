import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # match any n+1 to end of string b to any subset in a and
        # 0 to n of b to another subset of a
        if not set(b).issubset(set(a)):
            return -1

        multiplication_factor = math.ceil(len(b) / len(a))

        repeated = a * multiplication_factor
        if b in repeated:
            return multiplication_factor

        repeated += a
        if b in repeated:
            return multiplication_factor + 1

        return -1
