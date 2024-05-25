class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        def solve(start, path):
            if start >= len(s):
                ans.append(" ".join(path))
                return
            for i in range(start, len(s)):
                if s[start:i+1] in wordSet:
                    path.append(s[start:i+1])
                    solve(i + 1, path)
                    path.pop()
        ans = []
        solve(0, [])
        return ans
