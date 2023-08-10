class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        val = 0
        pre_curr = 0
        for i in range(len(s)):
            curr = dic[s[i]]
            if i != 0:
                pre_curr = dic[s[i - 1]]

            if pre_curr != 0 and curr > pre_curr:
                val = val + (curr - pre_curr) - pre_curr
                continue
            if curr > val:
                val = curr - val
            else:
                val = curr + val
        return val
