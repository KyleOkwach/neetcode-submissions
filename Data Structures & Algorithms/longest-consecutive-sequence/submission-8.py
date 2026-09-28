class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            seq = 0
            if n - 1 in nums_set:  # not start of a sequence
                continue
            while n + seq in nums_set:
                    seq += 1
            longest = max(longest, seq)
        
        return longest