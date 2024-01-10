class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        days = len(prices)
        for i in range(1, days):
            ans += 0 if prices[i] <= prices[i-1] else prices[i] - prices[i-1]
        return ans
