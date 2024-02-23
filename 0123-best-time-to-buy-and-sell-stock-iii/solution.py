class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(maxsize=None)
        def solve(pos, t, is_bought):
            if pos >= n or t == 0:
               return 0
            result = solve(pos + 1, t, is_bought)
            if is_bought:
                result = max(result, solve(pos + 1, t - 1, False) + prices[pos])
            else:
                result = max(result, solve(pos + 1, t, True) - prices[pos])
            return result
        return solve(0, 2, False)
            

