from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""
        for i in digits:
            number = number + str(i)
        number = int(number) + 1
        number = str(number)
        output = []
        for i in number:
            output.append(int(i))
        return output
