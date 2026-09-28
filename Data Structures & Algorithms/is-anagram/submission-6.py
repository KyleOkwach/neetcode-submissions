class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set, t_set = sorted(list(s)), sorted(list(t))
        return s_set == t_set