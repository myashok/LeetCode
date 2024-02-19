class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        position_val = defaultdict(list)
        row_max = [0]*m
        col_max = [0]*n
        max_path = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                position_val[mat[i][j]].append((i, j))

        ans = 1 
        for val in sorted(position_val, reverse=True):
            for position in position_val[val]:
                row, col = position
                max_path[row][col] = max(row_max[row], col_max[col]) + 1               
                     
            for position in position_val[val]:
                row, col = position
                row_max[row] = max(row_max[row], max_path[row][col])
                col_max[col] = max(col_max[col], max_path[row][col])
        
        return max(max(row_max), max(col_max))
