class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest = 0, 0
        res = set()
        
        for r in range(len(s)):
            if s[r] in res:
                while s[r] in res:
                    res.remove(s[l])
                    l += 1
            res.add(s[r])
            
            longest = max(longest, len(res))
        
        return longest
        