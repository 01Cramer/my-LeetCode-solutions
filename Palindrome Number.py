class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers = []
        if x < 0:
            return False
        while x > 0:
            x_mod = x % 10
            numbers.append(x_mod)
            x //= 10  # floor
        for i in range(len(numbers)):
            if numbers[i] != numbers[len(numbers) - 1 - i]:
                return False
        return True
