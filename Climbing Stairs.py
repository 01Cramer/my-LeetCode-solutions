import math


class Solution:
    def climbStairs(self, n: int) -> int:
        output = 1

        max_2 = n // 2

        while max_2 > 0:
            ones = n - max_2 * 2
            places = max_2 + ones

            output += math.comb(places, max_2)  # binomial coefficient
            max_2 -= 1
        return output
