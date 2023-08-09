class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        dic = {}  # Marking strings 0 - starting point, 1 - already found
        sorted_strs = []

        for string in strs:
            sorted_string = sorted(string)
            sorted_string = "".join(sorted_string)
            sorted_strs.append(sorted_string)

            dic[string] = 0

        for i in range(len(sorted_strs)):
            if dic[strs[i]] != 1:
                l1 = [strs[i]]
                for j in range(i + 1, len(sorted_strs)):
                    if sorted_strs[i] == sorted_strs[j]:
                        l1.append(strs[j])
                        dic[strs[j]] = 1  # Anagram found - marking with 1 in dic
                output.append(l1)
            else:
                continue
        return output
