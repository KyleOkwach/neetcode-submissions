class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        return list({k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True) }.keys())[:k]