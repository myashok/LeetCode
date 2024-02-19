class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        value_to_position = defaultdict(list)
        ans = 1
        dp = [[1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                value_to_position[mat[i][j]].append((i, j))
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for val in sorted(value_to_position, reverse=True):
            for row, col in value_to_position[val]:
                for dx, dy in direction:
                    new_row = row + dx
                    new_col = col + dy
                    if 0 <= new_row < m and 0 <= new_col < n and mat[new_row][new_col] > mat[row][col]:
                        dp[row][col] = max(dp[row][col], dp[new_row][new_col] + 1)
                        ans = max(ans, dp[row][col])
        return ans

