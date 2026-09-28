class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        i = 0  # index of smallest element
        
        while l <= r:
            m = (l + r) // 2  # center
            if nums[m] < nums[i]:
                if i > r:
                    l = m + 1
                else:
                    r = m
                i = m
            else:
                l = m + 1

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                m = (left + right) // 2  # center
                if nums[m] > target:
                    right = m - 1
                elif nums[m] < target:
                    left = m + 1
                else:
                    return m
            
            return -1
        
        res = binary_search(0, i - 1)
        if res != -1:
            return res
        
        return binary_search(i, len(nums) - 1)
        