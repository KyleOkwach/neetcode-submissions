class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set, t_set = sorted(list(s)), sorted(list(t))
        print(s_set, t_set)
        return s_set == t_set