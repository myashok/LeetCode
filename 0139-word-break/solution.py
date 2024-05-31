class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [0]*(n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                if len(w) <= i and s[i-len(w):i] == w and dp[i-len(w)]:
                    dp[i]  = True
                    break
        return dp[len(s)]
        
       
