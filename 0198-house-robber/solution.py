class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for index in range(1, n):
            dp[index] = max(dp[index-1], (dp[index-2] if index - 2 >= 0 else 0) + nums[index])
        
        return dp[n-1]   
        
