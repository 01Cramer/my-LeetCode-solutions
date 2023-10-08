class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        hamming_weight = 0
        for i in binary:
            if i == "1":
                hamming_weight += 1
        return hamming_weight
