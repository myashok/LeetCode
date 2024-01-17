class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0]*(k+1)
        mn = [prices[0]]*(k+1)
        n = len(prices)
        for i in range(n):
            for j in range(1,k+1):
                mn[j] = min(mn[j], prices[i] - dp[j-1])
                dp[j] = max(dp[j], prices[i] - mn[j])
        
        return dp[k]

