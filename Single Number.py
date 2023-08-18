from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if i != 0:
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    return nums[i]
                if (
                    i == len(nums) - 2
                    and nums[i] == nums[i - 1]
                    and nums[i] != nums[i + 1]
                ):
                    return nums[i + 1]

        return nums[0]
