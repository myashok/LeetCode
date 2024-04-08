class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        for rect in rectangles:
            l, h = rect
            mp[h].append(l)
        
        for key in mp:
            mp[key].sort()
        ans = []
        for point in points:
            x, y = point
            count = 0
            for h in range(y, 101):
                if h in mp:
                    count += len(mp[h]) - bisect.bisect_left(mp[h], x)
            ans.append(count)
        return ans

        
