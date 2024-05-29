class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        ans = 0
        while num != 1:
            if num & 1:
                num += 1
            else:
                num //= 2
            ans += 1
        return ans
    
