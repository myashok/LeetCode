class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def match(s, si, p, pi):
            if pi < 0:
                return si < 0
            if si < 0:
                return all([True if p[i] =='*' else False for i in range(pi, -1, -2)])
            
            if p[pi] == '.' or p[pi] == s[si]:
                return match(s, si-1, p, pi-1)

            if p[pi] == '*':
                return match(s, si, p, pi - 2) or (p[pi-1] in (s[si], '.') and match(s, si - 1, p, pi))
            return False

        return match(s, len(s) - 1, p, len(p) - 1)


