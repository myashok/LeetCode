class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        ciel_sqrt_n = floor(sqrt(n)) + 1
        for i in range(1,ciel_sqrt_n):
            perfect_squares.append(i*i)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n + 1):
            for perfect_square in perfect_squares:
                if perfect_square > i:
                    break
                else:
                    dp[i] = min(dp[i], dp[i-perfect_square] + 1)
        return dp[n]
        
