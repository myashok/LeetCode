class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal = ans = 0
        for c in s:
            if c == '(':
                bal += 1
            elif bal > 0:
                bal -= 1
            else:
                ans += 1
        return ans + bal


