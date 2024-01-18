class Solution:
    # [0, 2, 3] = (0, 1)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if s == s[::-1] or n == 1:
            return s

        dp = [[False]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        ans = (0, 1)
        
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    ans = (i, j+1)
        
        return s[ans[0]:ans[1]]
