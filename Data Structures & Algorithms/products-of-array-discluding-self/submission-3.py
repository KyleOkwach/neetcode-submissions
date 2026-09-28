class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        pre, post = 1, 1

        for i in range(len(nums)):
            out.append(pre)
            pre *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= post
            post *= nums[i]

        return out