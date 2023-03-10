class Solution:
   def isRectangleCover(self, rectangles):
        area = 0
        corners = set()
        a, c = lambda: (X - x) * (Y - y), lambda: {(x, y), (x, Y), (X, y), (X, Y)}
        for x, y, X, Y in rectangles:
            area += a()
            corners ^= c()
            
        if len(corners) != 4:
            return False
        x = min(coor[0] for coor in corners)
        y = min(coor[1] for coor in corners)
        X = max(coor[0] for coor in corners)
        Y = max(coor[1] for coor in corners)

        return area == a()    