class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        min_heap = []
        bricks_used = 0
        for i in range(1, n):
            height_diff = heights[i] - heights[i-1]
            if height_diff > 0:
                if len(min_heap) < ladders:
                    heapq.heappush(min_heap, height_diff)
                else:
                    bricks_used += heapq.heappushpop(min_heap, height_diff) 
                    if bricks_used > bricks:
                        return i - 1
            
        return n - 1
                
