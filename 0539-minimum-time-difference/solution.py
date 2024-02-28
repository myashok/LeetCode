class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ans = math.inf
        # print(timePoints)
        for i in range(1, len(timePoints)):
            curr_time = timePoints[i]
            prev_time = timePoints[i-1]
            curr_hour, curr_min = curr_time.split(':')
            prev_hour, prev_min = prev_time.split(':')
            time_diff = int(curr_hour) * 60  + int(curr_min) - int(prev_hour) * 60  - int(prev_min)
            ans = min(ans, min(24*60 - time_diff, time_diff))
        prev_time = timePoints[0]
        curr_time = timePoints[len(timePoints)-1]
        curr_hour, curr_min = curr_time.split(':')
        prev_hour, prev_min = prev_time.split(':')
        time_diff = int(curr_hour) * 60  + int(curr_min) - int(prev_hour) * 60  - int(prev_min)
        ans = min(ans, min(24*60 - time_diff, time_diff))
        return ans
