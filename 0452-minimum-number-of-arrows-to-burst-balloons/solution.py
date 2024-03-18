class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        merged_length = 1
        points.sort()
        prev_point = points[0]
        for curr_point in points[1:]:
            if prev_point[1] < curr_point[0]:
                prev_point =  curr_point
                merged_length += 1
            else:
                prev_point[1] = min(prev_point[1], curr_point[1])

        return merged_length
