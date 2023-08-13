from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        dic = {}
        for number in nums:
            if number not in dic:
                dic[number] = 1
            else:
                dic[number] += 1
        i = 0
        while i < k:
            most_freq = 0
            output_key = 0
            for key in dic:
                if dic[key] > most_freq:
                    most_freq = dic[key]
                    output_key = key
            output.append(output_key)
            del dic[output_key]
            i += 1
        return output
