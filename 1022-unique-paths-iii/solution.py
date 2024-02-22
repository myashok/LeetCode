from collections import deque
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        allowed_cell_cnt = 0
        source = target = None

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    allowed_cell_cnt += 1
                elif grid[i][j] == 1:
                    source = (i, j)

        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        
        def dfs(r, c, visited_allowed_cell_cnt):
            nonlocal ans
            if visited_allowed_cell_cnt == allowed_cell_cnt and grid[r][c] == 2:
                ans += 1
                return

            elif visited_allowed_cell_cnt >= allowed_cell_cnt:
                return

            grid_val, grid[r][c] = grid[r][c], -2

            for dx, dy in directions:
                new_r = r + dx
                new_c = c + dy
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] in (0, 2):
                    dfs(new_r, new_c, visited_allowed_cell_cnt + 1)

            grid[r][c] = grid_val
        
        dfs(source[0], source[1], -1)
        
        return ans
