class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = {}
        res = []
        for i, n in enumerate(nums):
            prods[i] = [j for k, j in enumerate(nums) if k != i]

        for i in prods.values():
            temp = 1
            for j in i:
                temp *= j
            res.append(temp)

        return res