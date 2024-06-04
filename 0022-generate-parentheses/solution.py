from functools import lru_cache


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        max_len = 2*n
        ans = []
        def solve(curr_path, open, close):
            if len(curr_path) == max_len:
                ans.append("".join(curr_path[:]))
                return
            if open < n:
                curr_path.append('(')
                solve(curr_path, open + 1, close)
                curr_path.pop()
            if open > close:
                curr_path.append(')')
                solve(curr_path, open, close + 1)
                curr_path.pop()
        solve([], 0, 0)
        return ans

