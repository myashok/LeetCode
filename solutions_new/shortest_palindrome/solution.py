class Solution:
    def shortestPalindrome(self, s: str) -> str:
        new_s = f'{s}#{s[::-1]}'
        pt_table = [0]*len(new_s)
        
        for i in range(1, len(pt_table)):
            t = pt_table[i-1]
            while t > 0 and new_s[i] != new_s[t]:
                t = pt_table[t-1]
            pt_table[i] = t + (new_s[i] == new_s[t])
            
        return new_s[len(s)+ 1: -pt_table[-1]] + s
        