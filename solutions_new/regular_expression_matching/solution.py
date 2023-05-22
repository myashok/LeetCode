from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def match(si: int, pi: int) -> bool:
            if pi < 0:
                return si < 0    
            if si < 0:
                return p[pi] == '*' and match(si, pi-2)      
            
            if p[pi] == '*':
                return (p[pi-1] in (s[si], '.') and match(si-1, pi)) or match(si, pi-2)
            else:
                return (p[pi] in (s[si], '.')) and match(si-1, pi-1)
            
        return match(len(s)-1, len(p)-1)
   