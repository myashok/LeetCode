class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_pos = min(arrLen - 1, steps//2)
        dp = [0]*(max_pos + 1)
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for i in range(1, steps+1):
            new_dp = dp[:]
            for j in range(max_pos + 1):
                if j > 0:
                    new_dp[j] += dp[j-1]%MOD
                if j < max_pos:
                    new_dp[j] += dp[j+1]%MOD
            dp = new_dp
        return dp[0] % MOD
