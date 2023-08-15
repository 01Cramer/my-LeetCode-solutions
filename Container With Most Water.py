from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        l = 0
        r = n - 1
        while l < r:
            x = r - l
            y = min(height[l], height[r])
            area = x * y
            if area > max_area:
                max_area = area
            if y == height[l]:
                l += 1
            else:
                r -= 1
        return max_area
