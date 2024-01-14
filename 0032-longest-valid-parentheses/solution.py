class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]*(len(s) + 1)
        for i, n in enumerate(s):
            if i == 0:
                continue
            if n == ')' and (i - 1 - dp[i-1] >= 0 and s[i-1-dp[i-1]] == '('):
                dp[i] = dp[i-1] + 2 + (dp[i-2-dp[i-1]] if i-2 - dp[i-1] >= 0 else 0)

        return max(dp)
