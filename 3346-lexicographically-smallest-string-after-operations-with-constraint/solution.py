class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans = []
        a_asc = ord('a')
        for c in s:
            asc = ord(c) - a_asc
            rotations = min(asc, 26 - asc)
            if rotations <= k:
                ans.append('a')
                k -= rotations
            else:
                ans.append(chr(a_asc + asc - k))
                k = 0
            if k == 0:
                return ''.join(ans) + s[len(ans):]
                
        return ''.join(ans)

