class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(u, v, gold):
            tmp = grid[u][v]
            grid[u][v] = 0
            max_gold = gold
            for i in range(4):
                new_u = u + x[i]
                new_v = v + y[i]
                if 0 <= new_u < m and 0 <= new_v < n and grid[new_u][new_v]:
                    max_gold = max(max_gold, dfs(new_u, new_v, gold + grid[new_u][new_v]))
            grid[u][v] = tmp
            return max_gold

        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:  # Start DFS only if the cell has gold
                    ans = max(ans, dfs(i, j, grid[i][j]))

        return ans

