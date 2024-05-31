class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        h = len(nums) - 1
        while l < h:
            mid = (l + h) // 2
            if (mid & 1 and nums[mid] != nums[mid-1]) or (not mid & 1 and nums[mid] != nums[mid + 1]):
                h = mid
            else:
                l = mid + 1
        return nums[l]

