class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = ans = curr_sum = 0
        for r, num in enumerate(nums):
            curr_sum += num
            while curr_sum + k < num * (r-l+1):
                curr_sum -= nums[l]
                l += 1
            else:
                ans = max(ans, r - l + 1)
        return ans
