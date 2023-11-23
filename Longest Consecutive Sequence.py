class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:  # edge cases
            return 1
        elif len(nums) == 0:
            return 0

        nums = sorted(nums)  # nlogn sort
        output = 1
        max_output = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                max_output += 1
                print(max_output)
            elif nums[i + 1] == nums[i]:
                continue
            else:
                if max_output >= output:
                    output = max_output
                    max_output = 1
                else:
                    max_output = 1

        if max_output > output:  # edge case if consecutive-sequence is ending loop
            output = max_output

        return output