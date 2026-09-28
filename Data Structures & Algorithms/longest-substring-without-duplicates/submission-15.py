class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        sub = set()

        for r in range(len(s)):
            if s[r] in sub:
                while s[r] in sub:
                    sub.remove(s[l])
                    l += 1
            sub.add(s[r])
            res = max(res, len(sub))
        
        return res