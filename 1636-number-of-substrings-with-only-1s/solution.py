class Solution:
    def numSub(self, s: str) -> int:
        bins = s.split('0') 
        ans = 0
        for bi in bins:
            n = len(bi)
            ans += (n * (n + 1))//2

        return ans % (10**9 + 7)
