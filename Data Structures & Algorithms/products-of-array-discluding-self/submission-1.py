class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, pre, post = [], [], []
        prod = 1
        
        for i in range(len(nums)):
            prod *= nums[i]
            pre.append(prod)

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            post.append(prod)
        
        post.reverse()
        print(pre, post)
        for i in range(len(nums)):
            if i <= 0:
                res.append(post[i + 1])
            elif i >= len(nums) - 1:
                res.append(pre[i - 1])
            else:
                res.append(pre[i - 1] * post[i + 1])

        return res