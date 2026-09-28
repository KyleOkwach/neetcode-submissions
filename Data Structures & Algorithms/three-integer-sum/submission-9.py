class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # remove duplicates
                continue
            if nums[i] > 0:  # considering the list is sorted
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    out.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    # Skip duplicates for the second element
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Skip duplicates for the third element
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return out
