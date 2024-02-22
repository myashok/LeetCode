class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        old_visited_count = 0
        ans = 0
        def dfs(r, c):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited.add((r, c))
            for dx, dy in directions:
                new_r = dx + r
                new_c = dy + c
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
                    dfs(new_r, new_c)

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j]:
                    dfs(i, j)
                    ans = max(ans, len(visited) - old_visited_count)
                    old_visited_count = len(visited) 
        return ans
