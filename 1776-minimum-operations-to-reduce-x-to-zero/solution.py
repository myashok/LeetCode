class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        k = sum(nums) - x
        l = 0
        ans = -1
        curr_sum = 0
        for r, num in enumerate(nums):
            curr_sum += num
            while curr_sum > k and l <= r:
                curr_sum -= nums[l]
                l += 1
            if curr_sum == k:
                ans = max(ans, r - l + 1)
        return -1 if ans == -1 else len(nums) - ans
