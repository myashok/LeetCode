from functools import lru_cache
class Solution:
    
            
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(maxsize=1000)
        def match(si: int, pi: int) -> bool:
            if pi == len(p):
                return len(s) == si
            
            if si == len(s):
                return p[pi] == "*" and match(si, pi+1)       
        
            if p[pi] == '*':
                return match(si+1, pi)  or match(si, pi+1)
            else:
                return (s[si] == p[pi] or p[pi] == '?') and match(si+1, pi+1)
            
        return match(0, 0)
            