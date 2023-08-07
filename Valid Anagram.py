class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            if char in t:
                t = t.replace(char, "", 1)
            else:
                return False
        if t == "":
            return True
        else:
            return False
        """
        if len(s) != len(t):
            return False
        s_dic = {}
        t_dic = {}
        for char in s:
            occurances = s.count(char)
            s_dic[char] = occurances
        for char in t:
            occurances = t.count(char)
            t_dic[char] = occurances
        for char in s_dic:
            if char in t_dic:
                if s_dic[char] != t_dic[char]:
                    return False
            else:
                return False
        return True
        """
        """
        if len(s) != len(t):
            return False
        for i in range():
            if char in t:
                occurances_in_s = s.count(char)
                occurances_in_t = t.count(char)
                if occurances_in_s != occurances_in_t:
                    return False
            else:
                return False
        return True
        """
