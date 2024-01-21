class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = prev_result = prev_prev_result = 0
        for num in nums:
            ans = max(prev_result, num+prev_prev_result)
            prev_prev_result = prev_result
            prev_result = ans
            
        return ans
