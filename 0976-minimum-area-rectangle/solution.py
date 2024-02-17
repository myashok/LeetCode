class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = {(x, y) for x, y in points}
        ans = float('inf')
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i+1:]:
                if x1 != x2 and y1 != y2 and (x1, y2) in points_set and (x2, y1) in points_set:
                    ans = min(ans, abs(x2 - x1)*abs(y2-y1))

        return 0 if ans == float('inf') else ans

