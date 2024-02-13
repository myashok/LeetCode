class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        for t in range(1, target + 1):
            n = t.bit_length()
            lb = 2**(n-1) - 1
            ub = 2**n - 1
            if ub == t:
                dp[t] = n
                continue
            # n A and 1 R
            dp[t] = n + 1 + dp[ub - t] 
            # n-1 A 1 R and mA and 1R and 
            for m in range(n-1):
                dp[t] = min(dp[t], n + m + 1 + dp[t - (lb) + (2**m-1)])
                
        return dp[target]
