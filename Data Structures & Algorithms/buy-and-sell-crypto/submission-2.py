class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = prices[0]  # buy

        for r in prices:
            max_profit = max(max_profit, r - l)
            l = min(l, r)
        
        return max_profit