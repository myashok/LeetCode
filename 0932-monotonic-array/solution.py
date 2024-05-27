class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        tone = None
        increasing = 1
        decreasing = 2
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] and not tone:
                tone = increasing
            elif nums[i] < nums[i-1] and not tone:
                tone = decreasing
            if nums[i] > nums[i-1] and tone == decreasing:
                return False
            elif nums[i] < nums[i-1] and tone == increasing:
                return False
        return True

