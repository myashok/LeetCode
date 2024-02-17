class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted([(num, i) for i, num in enumerate(nums)])
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l][0] + nums[r][0] < target:
                l += 1
            elif nums[l][0] + nums[r][0] > target:
                r -= 1
            else:
                return [nums[l][1], nums[r][1]]

