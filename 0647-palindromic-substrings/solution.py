class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp =[[False] * n for _ in range(n)]
        ans = n
        for i in range(n):
            dp[i][i] = True
        if n > 1:
            for i in range(n-1):
                dp[i][i+1] = s[i] == s[i+1]
                ans += s[i] == s[i+1]

        for l in range(3, n+1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans += 1
        return ans



