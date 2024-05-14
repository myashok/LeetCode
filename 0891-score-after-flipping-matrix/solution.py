class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        col_count = [0] * (len(grid[0]))
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            flag = False
            for j in range(n):
                if (j == 0 and grid[i][j]) or flag:
                    flag = True
                else:
                    grid[i][j] = not grid[i][j]
                col_count[j] += grid[i][j]
        for j in range(1, n):
            if col_count[j]  < ceil(m/2):
                for i in range(m):
                    grid[i][j] = not grid[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += (2** (n - j - 1)) * grid[i][j]
        return ans


        
