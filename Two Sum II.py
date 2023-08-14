from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        if numbers[l] >= 0:  # No negative values, target > 0
            while numbers[r] > target and r > 1:
                r -= 1
        else:  # Negative values
            while numbers[l] + numbers[r] < target and l < r:
                l += 1
            while numbers[l] + numbers[r] > target and l < r:
                r -= 1
        while l < r:
            for i in range(r):
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                else:
                    l += 1
            l = 0
            r -= 1
        return []
        """
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return [l+1, r+1]
        """
