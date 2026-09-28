class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        i = 0  # index of smallest element
        while l <= r:
            k = (l + r) // 2  # center
            if nums[k] < nums[i]:
                if i > r:
                    l = k + 1
                else:
                    r = k
                i = k
            else:
                l = k + 1
        
        return nums[i]