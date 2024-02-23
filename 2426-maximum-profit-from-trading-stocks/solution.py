class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        
        @lru_cache(maxsize=None)
        def solve(pos, budget):
            if pos >= len(present):
                return 0

            result = solve(pos + 1, budget)
            if future[pos] > present[pos] and budget >= present[pos]:
                result = max(result, solve(pos + 1, budget - present[pos]) + future[pos] - present[pos])
            return result

        result = solve(0, budget)
        solve.cache_clear()
        return result

