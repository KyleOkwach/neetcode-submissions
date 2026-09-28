class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        count_sorted = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
        return list(count_sorted)[:k]