class Solution:
    def numberOfWays(self, startPos, endPos, k):
        MOD = 10**9 + 7
        
        # Compute the required displacement
        d = endPos - startPos
        
        # Check if it's possible to reach in exactly k steps
        if (k + d) % 2 != 0 or abs(d) > k:
            return 0
        
        right_steps = (k + d) // 2
            
        # Calculate the binomial coefficient C(k, right_steps)
        result = comb(k, right_steps) % MOD
        return result
