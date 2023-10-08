class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bits_a = len(a)
        bits_b = len(b)
        value_a = 0
        value_b = 0
        for i in range(bits_a):
            if a[i] == "1":
                value_a += 2 ** (bits_a - 1 - i)
        for i in range(bits_b):
            if b[i] == "1":
                value_b += 2 ** (bits_b - 1 - i)
        result = value_a + value_b
        return bin(result)[2:]
