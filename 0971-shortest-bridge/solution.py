from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()  
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            q.append((i, j, 0))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Find the first island and mark it
        found_island = False
        for i in range(m):
            if found_island:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found_island = True
                    break

        # Explore the neighboring cells of the island
        while q:
            x, y, step = q.popleft()
            for dx, dy in direction:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < m and 0 <= new_y < n:
                    if grid[new_x][new_y] == 1:
                        return step
                    elif grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = 2
                        q.append((new_x, new_y, step + 1))

        return -1

