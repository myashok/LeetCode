class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # Compute prefix sum matrix
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

        # Iterate through all submatrices and count the ones that sum up to target
        count = 0
        for start_row in range(1, rows + 1):
                for end_row in range(start_row, rows + 1):
                    submatrix_sum = 0
                    has_submatrix_sum = defaultdict(int)
                    has_submatrix_sum[0] = 1
                    for col in range(1, cols + 1):
                        submatrix_sum = prefix_sum[end_row][col] - prefix_sum[start_row-1][col]
                        if submatrix_sum - target in has_submatrix_sum:
                            count += has_submatrix_sum[submatrix_sum - target]
                        has_submatrix_sum[submatrix_sum] += 1
        return count

