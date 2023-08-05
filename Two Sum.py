from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]+nums[j]==target):
                    output = [i,j]
                    return output
        """
        diff_and_index = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            diff_and_index[diff] = i
        for diff in diff_and_index:
            if diff in nums:
                if diff_and_index[diff] != nums.index(diff):
                    output = [diff_and_index[diff], nums.index(diff)]
                    return output
