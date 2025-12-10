class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_representation = bin(n)[2:]
        print(binary_representation)
        count = 0
        for d in binary_representation:
            if d == '1':
                count += 1
        return count