class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        count = 1
        nums = nums[1:]
        for num in nums:
            if count == 0:
                ans = num
            count += 1 if (ans == num) else -1
        return ans
