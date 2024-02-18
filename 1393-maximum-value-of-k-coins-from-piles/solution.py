class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:  
        @cache
        def dp(i, c):
            if c == 0 or i == len(piles): return 0
            res, cur = dp(i + 1, c), 0
            for j in range(min(len(piles[i]), c)):
                cur += piles[i][j]
                res = max(res, cur + dp(i+1, c-j-1))
            return res

        return dp(0, k)

