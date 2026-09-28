class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < len(nums) - 1:
                while l < r:
                    curr_sum = nums[i] + nums[l] + nums[r]
                    if curr_sum == 0:
                        if [nums[i], nums[l], nums[r]] not in out:
                            out.append([nums[i], nums[l], nums[r]])
                    r -= 1
                print(i, l, r)
                l += 1
                r = len(nums) - 1
        return out
