class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        
        @cache
        def solve(start_index, k): 
            if start_index == n or k <= 0:
                return 0
            return max(solve(start_index + 1, k), events[start_index][2] + solve(bisect.bisect_left(events, events[start_index][1] + 1, key=lambda x: x[0]), k - 1))
        
        return solve(0, k)
