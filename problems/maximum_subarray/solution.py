class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here = 0
        max_so_far = -10**5
        for num in nums:
            max_ending_here += num
            max_so_far = max(max_ending_here, max_so_far)
            max_ending_here = max(0, max_ending_here)
        return max_so_far