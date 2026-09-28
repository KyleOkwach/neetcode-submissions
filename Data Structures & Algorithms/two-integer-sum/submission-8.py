class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = { val: i for i, val in enumerate(nums) }

        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_map and nums_map[diff] != i:
                return [i, nums_map[diff]]