class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        res = 0

        while l < r:
            curr = 0
            if height[l] > height[r]:
                r -= 1
                curr = max(0, max_r - height[r])
            else:
                l += 1
                curr = max(0, max_l - height[l])
            print(curr, max_l, max_r)
            res += curr
            max_l, max_r = max(max_l, height[l]), max(max_r, height[r])
        
        return res