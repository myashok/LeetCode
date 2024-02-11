class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = ans = 0
        for r, num in enumerate(nums):
            if num == 0:
                k -= 1          
            while k < 0:
                k += (nums[l] == 0)
                l += 1
            ans = max(ans, r - l + 1)
        return ans
