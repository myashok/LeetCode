class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            grid[r][c] = index
            res = 0
            for dx, dy in directions:
                new_r = dx + r
                new_c = dy + c
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                    res += dfs(new_r, new_c)
            return res + 1
        index = 2
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
                    index += 1
        return ans
                    
