class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum = 1
        maximum = max(piles)
        k = maximum
        while minimum <= maximum:
            middle = (minimum + maximum) // 2
            hours_need = 0
            for i in range(len(piles)):
                hours_need += math.ceil(piles[i] / middle)

            if hours_need <= h and middle <= k:
                k = middle
                maximum = middle -1
            elif hours_need < h:
                maximum = middle - 1
            else:
                minimum = middle + 1
        return k
