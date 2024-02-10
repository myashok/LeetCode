class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l = matrix[0][0]
        h = matrix[n-1][n-1]
        def _is_count_of_no_smaller_or_equal_to_k(target: int) -> bool:
            col, row, cnt = n-1, 0, 0
            while row < n and col > -1:
                if matrix[row][col] <= target:
                    cnt += col + 1
                    row += 1
                else:
                    col -= 1
            return cnt > k - 1

        while l < h:
            mid = (l + h) // 2
            if _is_count_of_no_smaller_or_equal_to_k(mid):
                h = mid
            else:
                l = mid + 1

        return l
