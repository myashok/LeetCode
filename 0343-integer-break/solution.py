class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1

        d, m = n // 3, n % 3
        if m == 1:
            m = 4
            d -= 1
        return 3**d * m if m > 0 else 3**d
