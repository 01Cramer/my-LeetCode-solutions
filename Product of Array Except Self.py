class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = []
        postfix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
                postfix.append(0)
            else:
                prefix.append(prefix[i - 1] * nums[i])
                postfix.append(0)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i + 1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[i + 1])
            elif i == len(nums) - 1:
                output.append(prefix[i - 1])
            else:
                output.append(prefix[i - 1] * postfix[i + 1])
        return output