class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s,dict_t = {}, {}

        for i in s:
            dict_s[i] = 1 + dict_s.get(i, 0)
        for i in t:
            dict_t[i] = 1 + dict_t.get(i, 0)
        
        return dict_s == dict_t