class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=float("inf")
        profit=0

        for p in prices:
            low = min(low,p)
            profit=max(profit,p-low)
        return profit
        