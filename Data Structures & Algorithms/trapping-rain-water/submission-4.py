class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0
        res = 0

        # Get max to the right
        for i in range(len(height)):
            if i == r and i < len(height) - 1:
                r += 1
                for n in range(i + 1, len(height)):
                    if height[n] >= height[r]:
                        r = n
            curr = min(height[l], height[r]) - height[i]
            
            if curr > 0: res += curr
            if height[i] >= height[l]: l = i
        
        return res