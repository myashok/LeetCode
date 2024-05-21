class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def calculate(s, i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s) - 1:
                return 1
            ans = calculate(s, i + 1)
            if s[i: i + 2] <= '26':
                ans += calculate(s, i + 2)
            return ans
        return calculate(s, 0)
            
