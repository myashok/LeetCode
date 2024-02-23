class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(maxsize=None)
        def solve(pos, is_bought):
            if pos >= n:
               return 0
            result = solve(pos + 1, is_bought)
            if is_bought:
                result = max(result, solve(pos + 2, False) + prices[pos])
            else:
                result = max(result, solve(pos + 1, True) - prices[pos])
            return result

        return solve(0, False)
            

