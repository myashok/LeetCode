class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        @lru_cache(None)
        def solve(start):
            if start >= len(s):
                return True
            for i in range(start, len(s)):
                if s[start:i+1] in wordSet:
                    if solve(i + 1):
                        return True
            return False

        return solve(0)
        
