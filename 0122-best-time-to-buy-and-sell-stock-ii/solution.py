class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        ans = 0
        for sell in range(1, len(prices)):
            if prices[sell] > prices[buy]:
                ans += prices[sell] - prices[buy]
                buy = sell
            else:
                buy = sell
        return ans

