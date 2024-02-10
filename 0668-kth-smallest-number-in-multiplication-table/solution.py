class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l = 1
        h = m*n
        def _is_count_of_no_smaller_or_equal_to_k(target: int) -> bool:
            col, row, cnt = n, 1, 0
            while row <= m and col >= 1:
                if row * col <= target:
                    cnt += col
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
