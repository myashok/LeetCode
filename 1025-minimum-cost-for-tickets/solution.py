class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        
        @lru_cache(None)
        def dp(i):
            if i > days[-1]:
                return 0
            elif i in days_set:
                return min(
                    dp(i + 1) + costs[0],
                    dp(i + 7) + costs[1],
                    dp(i + 30) + costs[2]
                )
            else:
                return dp(i + 1)
        
        return dp(days[0])
