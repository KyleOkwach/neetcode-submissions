class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            cent = l + ((r - l) // 2)  

            if nums[cent] > target:
                r = cent - 1
            elif nums[cent] < target:
                l = cent + 1
            else:
                return cent
        return -1