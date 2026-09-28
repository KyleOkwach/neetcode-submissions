class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # O(n log n)

        for i in range(len(nums)):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early exit: if the current number is positive, no triplet can sum to 0
            if nums[i] > 0:
                break

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicates for the second element
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Skip duplicates for the third element
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
