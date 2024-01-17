class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [0]*n
        prev_min = prices[0]
        for i in range(1,n):
            dp[i] = max(0, prices[i] - prev_min, dp[i-1])
            prev_min = min(prev_min, prices[i])

        ans = dp[n-1]
        prev_max = prices[n-1]
        for i in range(n-3, -1, -1):
            ans = max(ans, prev_max - prices[i+1] + dp[i])
            prev_max = max(prev_max, prices[i+1])
        
        return ans    
