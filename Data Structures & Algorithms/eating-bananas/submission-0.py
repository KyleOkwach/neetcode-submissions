class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            h_taken = 0
            k = (l + r) // 2

            for p in piles:
                h_taken += math.ceil(p / k)
            
            if h_taken <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1
        
        return ans