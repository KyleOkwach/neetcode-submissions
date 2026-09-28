class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        for i in range(len(height)):
            if len(height[:i]) > 0:
                l, r = max(height[:i]), max(height[i:])
                curr = height[i]
                if curr < min(l, r):
                    res += min(l, r) - curr
        
        return res