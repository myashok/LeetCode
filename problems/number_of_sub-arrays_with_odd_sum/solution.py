class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        odd, even, res = 0, 0, 0
        for num in arr:
            if num & 1:
               odd, even = even, odd
               odd += 1
            else:
               even += 1
            res = (res + odd) % MOD
        return res