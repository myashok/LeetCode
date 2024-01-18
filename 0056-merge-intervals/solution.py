class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        prev_interval = intervals[0]
        index = 0
        for i in range(1,n):
            curr_interval = intervals[i]
            if prev_interval[1] >= curr_interval[0]:
                if prev_interval[1] < curr_interval[1]:
                    prev_interval[1] = curr_interval[1]
            else:
                intervals[index] = prev_interval
                prev_interval = curr_interval
                index += 1

        intervals[index] = prev_interval        
        
        return intervals[:index+1]



