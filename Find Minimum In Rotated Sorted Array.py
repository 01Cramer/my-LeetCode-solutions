class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            r_mid = mid + 1
            l_mid = mid - 1
            if mid == len(nums) - 1:
                r_mid = 0

            if nums[r_mid] < nums[mid]:
                return nums[r_mid]
            elif nums[r_mid] > nums[mid] and nums[l_mid] > nums[mid]:
                return nums[mid]
            else:
                if nums[mid] > nums[0]:
                    start = mid + 1
                else:
                    end = mid - 1

        return nums[0]