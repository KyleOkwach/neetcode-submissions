class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = s.count(s[i])
            count_t[t[i]] = t.count(t[i])
        
        return count_s == count_t