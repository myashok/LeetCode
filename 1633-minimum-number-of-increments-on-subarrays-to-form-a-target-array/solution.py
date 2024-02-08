class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = ans = 0
        for c in target:
            if c > prev:
                ans += c-prev
            prev = c
        return ans

