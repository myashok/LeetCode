from functools import lru_cache


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        list = []
        max_len = 2*n
        
        # @lru_cache(None)
        def helper(s, open, close):
            if len(s) == max_len:
                list.append(s)
                return    
            
            if open < n:
                helper(s + "(", open + 1, close)
            if close < open:
                helper(s + ")", open, close + 1)
  
        helper("", 0, 0)
        return list         
            