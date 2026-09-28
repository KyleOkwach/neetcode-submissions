class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxf = 0, 0
        res = 0
        counter = defaultdict(int)

        for r in range(len(s)):
            counter[s[r]] += 1
            maxf = max(maxf, counter[s[r]])
            
            while (r - l) + 1 - maxf > k:
                counter[s[l]] -= 1
                l += 1
                    

            res = max(res, (r - l) + 1)
        
        return res