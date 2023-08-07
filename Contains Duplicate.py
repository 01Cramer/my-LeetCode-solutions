from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        test_set = set([])
        for number in nums:
            test_set.add(number)
        if len(nums) != len(test_set):
            return True
        else:
            return False
