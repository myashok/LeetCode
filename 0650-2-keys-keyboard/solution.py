from functools import lru_cache
import math

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        @lru_cache(None)
        def calculate(curr_len, clipboard_len):
            if curr_len == n:
                return 0
            if curr_len > n:
                return math.inf

            paste = calculate(curr_len + clipboard_len, clipboard_len) + 1
            copy_paste = math.inf
            if clipboard_len != curr_len:
                copy_paste = calculate(curr_len, curr_len) + 1

            return min(paste, copy_paste)

        return calculate(1, 1) + 1
