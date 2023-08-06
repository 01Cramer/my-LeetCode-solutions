from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        while shortest != "":
            matches = 0
            for string in strs:
                if string[: len(shortest)] == shortest:
                    matches += 1
            if matches == len(strs):
                return shortest
            shortest = shortest[:-1]
        return ""
