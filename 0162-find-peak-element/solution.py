class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-math.inf] + nums + [-math.inf]
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l - 1

