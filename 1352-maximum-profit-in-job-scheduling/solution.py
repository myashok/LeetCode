class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        zip_index = sorted(list(zip(startTime, endTime, profit)))
        n = len(zip_index)
        @cache
        def solve(start_index): 
            if start_index == n:
                return 0
            res = zip_index[start_index][2] + solve(bisect.bisect_left(zip_index, zip_index[start_index][1], key=lambda x: x[0]))
            res = max(solve(start_index + 1), res)
            return res
        return solve(0)
