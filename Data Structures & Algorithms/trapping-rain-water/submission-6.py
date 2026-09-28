class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = [0] * len(height)
        max_r = [0] * len(height)
        max_n, res = 0, 0
        
        for l in range(len(height)):
            max_l[l] = max_n
            max_n = max(max_n, height[l])
            
        max_n = 0
        for r in range(len(height) - 1, -1, -1):
            max_r[r] = max_n
            max_n = max(max_n, height[r])
        
        for i in range(len(height)):
            curr = min(max_l[i], max_r[i]) - height[i]
            if curr > 0:
                res += curr

        return res