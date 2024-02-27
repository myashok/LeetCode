class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = intervals[0][1]
        cnt = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                cnt += 1
                end = min(intervals[i][1], end)
        return cnt
