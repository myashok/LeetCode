class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = curr_sum = 0
        ans = float('inf')
        for r, num in enumerate(nums):
            curr_sum += num
            while curr_sum >= target:
                if r - l + 1 < ans:
                    ans = r - l + 1
                curr_sum -= nums[l]
                l += 1
            if ans == 1:
                return ans
        return 0 if ans == float('inf') else ans
