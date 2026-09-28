class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in nums_set:
                seq = 1
                while n + seq in nums_set:
                    seq += 1 
                longest = max(longest, seq)
        
        return longest