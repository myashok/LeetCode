from functools import lru_cache


class Solution:
    @lru_cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            return 1/self.myPow(x, -n)
        
        if n % 2:
            return x * self.myPow(x, n-1)
        else:
            return self.myPow(x*x, n/2)
            
