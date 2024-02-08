class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] == target
            
        res = curr_sum = 0
        has_sum = {0: -1}
        for i in range(n):
            curr_sum += nums[i]
            required_sum = curr_sum - target
            if required_sum in has_sum:
                res += 1
                has_sum = {}
                curr_sum = 0
            has_sum[curr_sum] = res
        return res
