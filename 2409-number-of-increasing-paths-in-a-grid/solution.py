class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        position_val = defaultdict(list)
        max_path_val = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                position_val[grid[i][j]].append((i, j))
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def is_safe(i, j):
            return 0 <= i < m and 0 <= j < n
        
        ans = 0
        mod = (10**9 + 7)
        for val in sorted(position_val, reverse=True):
            for row, col in position_val[val]:
                temp = 1
                for dx, dy in direction:
                    new_row = row + dx
                    new_col = col + dy
                    if is_safe(new_row, new_col) and grid[new_row][new_col] > grid[row][col]:
                        temp += max_path_val[new_row][new_col]
                ans += temp
                max_path_val[row][col] = temp
                ans %= (mod)
                
        return ans % (mod)
