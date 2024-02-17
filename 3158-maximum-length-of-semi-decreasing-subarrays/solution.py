class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        reverse_mn = [0]*n
        reverse_mn[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            reverse_mn[i] = min(nums[i], reverse_mn[i+1])
        ans = 0
        for i, num in enumerate(nums):
            if n - i <= ans:
                return ans
            p = bisect.bisect_right(reverse_mn, num-1)
            if p > i:
                ans = max(ans, p - i)
        return ans


