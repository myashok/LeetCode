from typing import List

class Solution:
    def __init__(self):
        self.memo = collections.defaultdict(list) #memoize

    def partition(self, s: str) -> List[List[str]]:
        # Step 1: Precompute the palindrome substrings using dynamic programming
        if not s:
            return [[]]
        output = []
        if s in self.memo:
            return self.memo[s]

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
        
        # Check for palindromes of length greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

        # Step 2: Use backtracking to find all palindromic partitions
        def backtrack(start, path):
            if start == n:
                result.append(path)
                return
            for end in range(start, n):
                if dp[start][end]:
                    backtrack(end + 1, path + [s[start:end + 1]])

        result = []
        backtrack(0, [])
        self.memo[s] = result
        return result

