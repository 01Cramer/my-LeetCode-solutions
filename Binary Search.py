class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1

        while first <= last:
            middle = (first + last) // 2

            if nums[middle] < target:
                first = middle + 1
            elif nums[middle] > target:
                last = middle - 1
            else:
                return middle

        return -1