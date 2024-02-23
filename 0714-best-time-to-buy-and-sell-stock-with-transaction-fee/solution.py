class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @lru_cache(maxsize=None)
        def solve(pos, is_bought):
            if pos >= n:
               return 0
            result = solve(pos + 1, is_bought)
            if is_bought:
                result = max(result, solve(pos + 1, False) + prices[pos] - fee)
            else:
                result = max(result, solve(pos + 1, True) - prices[pos])
            return result
        return solve(0, False)
            

