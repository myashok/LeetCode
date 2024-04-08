class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        median_index =  n//2
        ans = 0
        if median <= k:
            for i in range(median_index, n):
                if k > nums[i]:
                    ans += max(k - nums[i], 0)
        else:
            for i in range(median_index + 1):
                if k < nums[i]:
                    ans += max(nums[i] - k, 0)

        return ans
        
